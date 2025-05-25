import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL = "codellama/CodeLlama-7b-hf"
hf_token = os.getenv("HUGGINGFACE_TOKEN")

def generate_test(prompt, output_file):
    tokenizer = AutoTokenizer.from_pretrained(MODEL, token=hf_token)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL,
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
  for tag, prompt in prompts.items():
    generate_test(prompt, f"output_codellama_direct_{tag}.txt")