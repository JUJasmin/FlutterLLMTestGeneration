# Flutter LLM Test Generation

This repository contains the setup, scripts, and results from an empirical research project evaluating Large Language Models' (LLMs) ability to generate Flutter widget tests.

## Repository Structure

* **Phase I/**

  * Contains Python scripts and generated outputs from the initial phase, testing multiple LLM models with varying prompt complexity.

* **Phase II/**

  * Includes Python scripts and outputs from the second phase, where selected promising models from Phase I were tested on more complex Flutter widgets.

* **SonarQube/**

  * Setup files and instructions for integrating SonarQube for automated test evaluation and code coverage analysis.

* **Setupscript/**

  * `setup_flutter_test_env_with_token.sh` – A bash script for quickly setting up the required environment, installing dependencies, and authenticating Hugging Face tokens.

## Methodology

The project was structured into two phases:

### Phase I: Prompt Variant Comparison

* Evaluated 10 LLMs (e.g., GPT-4, LLaMA-2-7B, Code LLaMA) on basic widget test generation.
* Prompt styles: Direct, Few-shot (1 example), Few-shot (2 examples).
* Evaluation: Output Quality, Semantic Accuracy, and Correctness (FC: Functionally Correct, FI: Functionally Incorrect, SI: Syntactically Incorrect).

### Phase II: Complex Test Capability Analysis

* Focused on four top-performing models from Phase I (GPT-4, DeepSeek, LLaMA-2-7B, CodeLLaMA).

* Evaluated performance on more complex Flutter widgets:

  * `ExpandableCard` (stateful interaction)
  * `ValidatedLoginForm` (form validation)
  * `PaginatedList` (asynchronous pagination)

* Metrics: Test correctness, code coverage (via SonarQube and `lcov`)

## Environment Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/JUJasmin/FlutterLLMTestGeneration.git
   cd FlutterLLMTestGeneration
   ```

2. Run the setup script (make sure to update with your Hugging Face token):

   ```bash
   bash Setupscript/setup_flutter_test_env_with_token.sh
   ```

## Running the Experiments

### Phase I

1. Navigate to the Phase I directory:

   ```bash
   cd Phase\ I
   ```

2. Run the Python scripts for each model:

   ```bash
   python run_tests_gpt4.py
   python run_tests_codellama.py
   # ...other model scripts
   ```

### Phase II

1. Navigate to the Phase II directory:

   ```bash
   cd ../Phase\ II
   ```

2. Execute tests for complex widgets:

   ```bash
   python run_complex_tests_gpt4.py
   python run_complex_tests_codellama.py
   # ...other selected model scripts
   ```

## Code Coverage and Analysis (SonarQube)

1. Navigate to the SonarQube folder:

   ```bash
   cd ../SonarQube
   ```

2. Follow the instructions in the `README.md` provided within the SonarQube folder to set up code coverage analysis and obtain detailed metrics.

## Interpreting Results

Results from both phases are categorized into:

* **Functionally Correct (FC)**: Fully functional and correct tests.
* **Functionally Incorrect (FI)**: Tests executed but logic errors were present.
* **Syntactically Incorrect (SI)**: Failed to compile or run.

Review the tables and output files in each phase folder for detailed model performance.

## Citation

If you find this repository useful in your research, please cite:

```
@misc{your_name2025flutterllm,
  author = {Your Name},
  title = {Evaluating Large Language Models for Flutter Test Generation},
  year = {2025},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/JUJasmin/FlutterLLMTestGeneration}}
}
```

## Acknowledgments

We thank our supervisors, collaborators at Thule, and colleagues from the School of Engineering for their valuable insights and contributions to this research project.
