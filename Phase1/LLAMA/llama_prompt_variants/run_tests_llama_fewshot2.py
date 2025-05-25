from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import os

def generate_flutter_test():
    model_name = os.getenv("MODEL_NAME", "meta-llama/Llama-7B-hf")
    prompt = """You are a helpful assistant that writes Flutter widget tests using the `flutter_test` package.

Here are two example widgets and their tests from the Flutter Testing App:

```dart
// Example 1: CounterApp
class CounterApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Center(child: TextButton(
          key: Key('increment'),
          onPressed: () {/* ... */},
          child: Text('+'),
        )),
      ),
    );
  }
}

// Test 1:
testWidgets('CounterApp increments when button tapped', (WidgetTester tester) async {
  await tester.pumpWidget(CounterApp());
  await tester.tap(find.byKey(Key('increment')));
  await tester.pump();
  expect(find.text('1'), findsOneWidget);
});

// Example 2: FavoritesItem
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

// Test 2:
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
```"""
    print(f"Loading model: {model_name}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",
        torch_dtype=torch.float32
    )
    model.eval()
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=300,
            do_sample=False,
            eos_token_id=tokenizer.eos_token_id
        )
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    with open("output_llama_fewshot2.txt", "w") as f:
        f.write(result)
    print("Output written to output_llama_fewshot2.txt")

if __name__ == "__main__":
    generate_flutter_test()
