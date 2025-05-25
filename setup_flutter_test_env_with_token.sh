#!/bin/bash

echo "Updating package lists..."
apt update

echo "Installing unzip and nano..."
apt install -y unzip nano

echo "Installing zip..."
apt install zip

echo "Installing Python dependencies for OpenAI and local models..."
pip install 'openai>=1.0.0' transformers accelerate torch

echo "Setting up environment variables..."
export OPENAI_API_KEY="Enter Your OpenAI Key Here"
export HUGGINGFACE_TOKEN="Enter Your Hugging Face Token Here - Be sure to ask for all required models used in this research paper"

echo "Creating directory structure..."
mkdir -p ~/flutter_test_gen
cd ~/flutter_test_gen

echo "Copying test runner scripts..."
cp /workspace/run_tests_*.py .
cp /workspace/run_all_tests.sh 2>/dev/null || true
cp /workspace/run_all_local_tests.sh 2>/dev/null || true

echo "Setup complete. You can now run tests!"
