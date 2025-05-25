from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import os

def generate_flutter_test():
    model_name = os.getenv("MODEL_NAME", "Salesforce/codet5-base")
    prompt = """You are a helpful assistant that writes Flutter widget tests using the `flutter_test` package.

Here is an example widget from the Flutter Testing App and its test:

```dart
// Example widget: FavoritesItem
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

// Corresponding test:
testWidgets('FavoritesItem shows filled heart when favorite', (WidgetTester tester) async {
  await tester.pumpWidget(MaterialApp(
    home: FavoritesItem(item: 'Apple', isFavorite: true),
  ));
  expect(find.byIcon(Icons.favorite), findsOneWidget);
});


Now write a widget test for this widget:
class ProfileAvatar extends StatelessWidget {
  final String imageUrl;
  const ProfileAvatar({required this.imageUrl, super.key});

  @override
  Widget build(BuildContext context) {
    return CircleAvatar(
      backgroundImage: NetworkImage(imageUrl),
    );
  }
}"""

    print(f"Loading model: {model_name}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(
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
    with open("output_codet5_fewshot1.txt", "w") as f:
        f.write(result)
    print("Output written to output_codet5_fewshot1.txt")

if __name__ == "__main__":
    generate_flutter_test()
