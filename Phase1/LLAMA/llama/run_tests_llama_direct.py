from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import os

def generate_flutter_test():
    model_name = os.getenv("MODEL_NAME", "meta-llama/Llama-2-7B-hf")
    prompt = """Write a Flutter widget test for the following widget from the Flutter Testing App sample:

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

The test should verify that the `ProfileAvatar` widget renders a `CircleAvatar` with the correct image."""
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
    with open("output_llama_direct.txt", "w") as f:
        f.write(result)
    print("Output written to output_llama_direct.txt")

if __name__ == "__main__":
    generate_flutter_test()
