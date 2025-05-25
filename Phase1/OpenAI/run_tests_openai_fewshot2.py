from openai import OpenAI
import os

def generate_flutter_test():
    client = OpenAI()
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
}
"""
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
    with open("output_openai_fewshot2.txt", "w") as f:
        f.write(output)
    print("Output written to output_openai_fewshot2.txt")

if __name__ == "__main__":
    generate_flutter_test()
