# Project Setup Instructions

This guide will help you set up the project and install all required dependencies.

## 1. Create a Virtual Environment (Recommended)

Using a virtual environment ensures that dependencies are isolated and prevents conflicts with other Python packages.

# Create a virtual environment named 'venv'
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate

## 2. Install Project Dependencies

To install all Python packages required for this project, run:

pip install -r requirements.txt

This ensures that all libraries and modules your project depends on are installed in your environment.

## 3. Install Local Library (UIAutomationLib)

If your project includes a local library (`UIAutomationLib`), install it in **editable mode**. This allows you to modify the library code without reinstalling it:

pip install -e .

## 4. Verify Installation

Check that all dependencies and the local library are installed correctly:

pip list

You should see all required packages listed, along with `UIAutomationLib`.

## 5. Run Tests with Output Directory

    robot -d <output_path>  <test_file_name or tests_folder_name>
                                (or)
    robot -outputdir <output_path>  <test_file_name or tests_folder_name>
