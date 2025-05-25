from openai import OpenAI
import os

def generate_flutter_test():
    client = OpenAI()
    prompt = """Write a Flutter widget test for the following widget:

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
    with open("output_openai_direct.txt", "w") as f:
        f.write(output)
    print("Output written to output_openai_direct.txt")

if __name__ == "__main__":
    generate_flutter_test()
