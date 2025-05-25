import os
from openai import OpenAI

client = OpenAI()

prompts = {
    "expandable": """You are a helpful assistant that writes Flutter widget tests using the `flutter_test` package. Write a Flutter widget test for a stateful widget that toggles its content with an expand icon button. The widget should show a title by default and reveal a description only when expanded. Test initial state, expanded state, and collapse state.

```dart

class ExpandableCard extends StatefulWidget {
  final String title;
  final String description;

  const ExpandableCard({
    required this.title,
    required this.description,
    super.key,
  });

  @override
  State<ExpandableCard> createState() => _ExpandableCardState();
}

class _ExpandableCardState extends State<ExpandableCard> {
  bool _isExpanded = false;

  void _toggleExpand() {
    setState(() {
      _isExpanded = !_isExpanded;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Column(
        children: [
          ListTile(
            title: Text(widget.title),
            trailing: IconButton(
              icon: Icon(_isExpanded ? Icons.expand_less : Icons.expand_more),
              onPressed: _toggleExpand,
            ),
          ),
          if (_isExpanded)
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: Text(widget.description),
            ),
        ],
      ),
    );
  }
}

```


""",
    "validation": """You are a helpful assistant that writes Flutter widget tests using the `flutter_test` package. Write a Flutter widget test for a login form that uses TextFormField and validates the email address. The form should disable the submit button until a valid email is entered. Test invalid and valid input states and ensure submit logic is conditionally enabled.

```dart
class LoginFormValidation extends StatefulWidget {
  const LoginFormValidation({super.key});

  @override
  State<LoginFormValidation> createState() => _LoginFormValidationState();
}

class _LoginFormValidationState extends State<LoginFormValidation> {
  final _formKey = GlobalKey<FormState>();
  final _usernameController = TextEditingController();

  bool get _isValid => _formKey.currentState?.validate() ?? false;

  @override
  Widget build(BuildContext context) {
    return Form(
      key: _formKey,
      child: Column(
        children: [
          TextFormField(
            key: const Key('username'),
            controller: _usernameController,
            decoration: const InputDecoration(labelText: 'Username'),
            validator: (value) =>
                (value != null && value.contains('@')) ? null : 'Username is email',
          ),
          ElevatedButton(
            key: const Key('submit'),
            onPressed: _isValid ? () {} : null,
            child: const Text('Submit'),
          )
        ],
      ),
    );
  }
}
```
""",
    "pagination": """You are a helpful assistant that writes Flutter widget tests using the `flutter_test` package. Write a Flutter widget test for a ListView that loads items in batches (pagination) as the user scrolls. Ensure that items are loaded on scroll to the bottom and that a loading indicator is shown during fetch.

```dart
class ListPage extends StatefulWidget {
  const ListPage({super.key});

  @override
  State<ListPage> createState() => _ListPageState();
}

class _ListPageState extends State<ListPage> {
  final List<String> _items = [];
  bool _isLoading = false;
  int _page = 0;

  @override
  void initState() {
    super.initState();
    _loadMore();
  }

  Future<void> _loadMore() async {
    setState(() => _isLoading = true);
    await Future.delayed(const Duration(milliseconds: 500));
    setState(() {
      _items.addAll(List.generate(20, (i) => 'Item \${_page * 20 + i + 1}'));
      _isLoading = false;
      _page++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return NotificationListener<ScrollNotification>(
      onNotification: (scroll) {
        if (!scroll.metrics.atEdge || _isLoading) return false;
        if (scroll.metrics.pixels == scroll.metrics.maxScrollExtent) {
          _loadMore();
        }
        return true;
      },
      child: ListView.builder(
        itemCount: _items.length + (_isLoading ? 1 : 0),
        itemBuilder: (context, index) {
          if (index >= _items.length) {
            return const Center(child: CircularProgressIndicator());
          }
          return ListTile(title: Text(_items[index]));
        },
      ),
    );
  }
}
```
"""
}

def generate(prompt, tag):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            { "role": "system", "content": "You are a helpful assistant that writes Flutter widget tests." },
            { "role": "user", "content": prompt }
        ],
        temperature=0.2,
        max_tokens=800
    )
    with open(f"output_gpt4_openai_direct{tag}.txt", "w") as f:
        f.write(response.choices[0].message.content.strip())

if __name__ == "__main__":
    for tag, prompt in prompts.items():
        generate(prompt, tag)