# LLMTestForge

**LLMTestForge** is a lightweight testing framework designed to process structured JSON data and generate human-readable HTML summaries. The project provides utilities for handling API responses, testing structured data, and generating summary reports.

## Features

- **JSON to HTML Summary Conversion**: Parses structured JSON files and generates readable HTML reports.
- **API Response Testing**: Includes scripts to test API outputs and validate expected results.
- **Flexible Input Handling**: Supports multiple input files for batch processing.

## Project Structure

- **`input/`** – Directory for input JSON files.
- **`output/`** – Directory where generated HTML reports are stored.
- **`api_test.py`** – Script for testing API responses.
- **`api_test_no_files.py`** – Variation of API testing without file-based input.
- **`generate_summary_html_from_json.py`** – Converts JSON summaries into an HTML report.
- **`generate_test_html_from_json.py`** – Processes test result JSON files and generates an HTML report.
- **`summary_json_structure.json`** – Example JSON structure for summary generation.
- **`test_json_structure.json`** – Example JSON structure for test case processing.
- **`.gitignore`** – Specifies ignored files and directories.
- **`LICENSE`** – Project licensing information.
- **`README.md`** – This documentation file.

## Installation

Clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/yuvalakavian/LLMTestForge.git
cd LLMTestForge
pip install -r requirements.txt
```

## Usage

1. **Generate an HTML Summary from JSON**:

   ```bash
   python generate_summary_html_from_json.py summary_json_structure.json
   ```

2. **Generate an HTML Test Report from JSON**:

   ```bash
   python generate_test_html_from_json.py test_json_structure.json
   ```

3. **Run API Tests**:

   ```bash
   python api_test.py
   ```

   or without file input:

   ```bash
   python api_test_no_files.py
   ```

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
