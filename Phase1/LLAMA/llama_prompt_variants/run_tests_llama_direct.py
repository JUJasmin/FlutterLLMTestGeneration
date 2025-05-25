import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "meta-llama/Llama-2-7b-chat-hf"
hf_token = os.getenv("HUGGINGFACE_TOKEN")

def generate_flutter_test(prompt, output_file):
    tokenizer = AutoTokenizer.from_pretrained(
        model_name,
        token=hf_token
    )
    
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",
        torch_dtype=torch.float16,
        token=hf_token
    )

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_new_tokens=300, do_sample=False)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)

    with open(output_file, 'w') as file:
        file.write(result)

if __name__ == "__main__":
    # Direct Prompt
    direct_prompt = '''Write a Flutter widget test for the following widget from the Flutter Testing App sample:

```dart
class ProfileAvatar extends StatelessWidget {
  final String imageUrl;
  const ProfileAvatar({required this.imageUrl, super.key});

  @override
  Widget build(BuildContext context) {
    return CircleAvatar(
      backgroundImage: NetworkImage(imageUrl),
    );
  }
}
```
The test should verify that the `ProfileAvatar` widget renders a `CircleAvatar` with the correct image.'''
    generate_flutter_test(direct_prompt, "output_llama_direct.txt")

    # Few-Shot 1 Prompt
    fewshot1_prompt = '''You are a helpful assistant that writes Flutter widget tests using the `flutter_test` package.

Here is an example widget from the Flutter Testing App and its test:

```dart
class FavoritesItem extends StatelessWidget {
  final String item;
  final bool isFavorite;
  const FavoritesItem({required this.item, required this.isFavorite, super.key});

  @override
  Widget build(BuildContext context) {
    return ListTile(
      title: Text(item),
      trailing: Icon(isFavorite ? Icons.favorite : Icons.favorite_border),
    );
  }
}

testWidgets('FavoritesItem shows filled heart when favorite', (WidgetTester tester) async {
  await tester.pumpWidget(MaterialApp(
    home: FavoritesItem(item: 'Apple', isFavorite: true),
  ));
  expect(find.byIcon(Icons.favorite), findsOneWidget);
});
```

Now write a widget test for this widget:

```dart
class ProfileAvatar extends StatelessWidget {
  final String imageUrl;
  const ProfileAvatar({required this.imageUrl, super.key});

  @override
  Widget build(BuildContext context) {
    return CircleAvatar(
      backgroundImage: NetworkImage(imageUrl),
    );
  }
}
```'''
    generate_flutter_test(fewshot1_prompt, "output_llama_fewshot1.txt")

    # Few-Shot 2 Prompt
    fewshot2_prompt = '''You are a helpful assistant that writes Flutter widget tests using the `flutter_test` package.

Here are two example widgets and their tests from the Flutter Testing App:

```dart
class CounterApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Center(child: TextButton(
          key: Key('increment'),
          onPressed: () {},
          child: Text('+'),
        )),
      ),
    );
  }
}

testWidgets('CounterApp increments when button tapped', (WidgetTester tester) async {
  await tester.pumpWidget(CounterApp());
  await tester.tap(find.byKey(Key('increment')));
  await tester.pump();
  expect(find.text('1'), findsOneWidget);
});

class FavoritesItem extends StatelessWidget {
  final String item;
  final bool isFavorite;
  const FavoritesItem({required this.item, required this.isFavorite, super.key});

  @override
  Widget build(BuildContext context) {
    return ListTile(
      title: Text(item),
      trailing: Icon(isFavorite ? Icons.favorite : Icons.favorite_border),
    );
  }
}

testWidgets('FavoritesItem shows filled heart when favorite', (WidgetTester tester) async {
  await tester.pumpWidget(MaterialApp(
    home: FavoritesItem(item: 'Apple', isFavorite: true),
  ));
  expect(find.byIcon(Icons.favorite), findsOneWidget);
});
```

Now write a widget test for this widget:

```dart
class ProfileAvatar extends StatelessWidget {
  final String imageUrl;
  const ProfileAvatar({required this.imageUrl, super.key});

  @override
  Widget build(BuildContext context) {
    return CircleAvatar(
      backgroundImage: NetworkImage(imageUrl),
    );
  }
}
```'''
    generate_flutter_test(fewshot2_prompt, "output_llama_fewshot2.txt")
