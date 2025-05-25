from openai import OpenAI
import os

def generate_flutter_test():
    client = OpenAI()
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
    response = client.chat.completions.create(
        model=os.getenv("MODEL_NAME", "gpt-4"),
        messages=[
            {"role": "system", "content": "You are a helpful assistant that writes Flutter tests."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=500
    )
    output = response.choices[0].message.content
    with open("output_openai_fewshot1.txt", "w") as f:
        f.write(output)
    print("Output written to output_openai_fewshot1.txt")

if __name__ == "__main__":
    generate_flutter_test()
