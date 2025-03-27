# LLMTestForge

LLMTestForge is a lightweight testing framework designed to process structured JSON data and generate human-readable HTML summaries. The project provides utilities for handling structured data and generating summary reports.

## Features

- **JSON to HTML Summary Conversion**: Parses structured JSON files and generates readable HTML reports.
- **Flexible Input Handling**: Supports multiple input files for batch processing.

## Project Structure

- `input/` – Directory containing input JSON files for processing.
- `output/` – Directory where generated HTML summaries are stored.
- `generate_summary_html_from_json.py` – Converts JSON data into HTML summary reports.
- `generate_test_html_from_json.py` – Generates HTML representations of test results from JSON data.
- `generate_json.py` – Script to generate structured JSON data.
- `summary_json_structure.json` – Sample JSON structure for summaries.
- `test_json_structure.json` – Sample JSON structure for test cases.

## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yuvalakavian/LLMTestForge.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd LLMTestForge
   ```

3. **Install Dependencies**:
   Ensure you have Python installed. Install required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare Input Data**:
   Place your JSON files in the `input/` directory. Use the provided `summary_json_structure.json` and `test_json_structure.json` as templates for your data.

5. **Run the Scripts**:
   - To generate structured JSON data:
     ```bash
     python generate_json.py
     ```
   - To generate HTML summaries:
     ```bash
     python generate_summary_html_from_json.py
     ```
   - To generate test results in HTML:
     ```bash
     python generate_test_html_from_json.py
     ```
   - To generate a test or summary from PDF or PPTX files:
     ```bash
     python generate_json.py --generate-type <test|summary> --file-type <pdf|pptx>
     ```
     - `--generate-type` (`-g`): Specify whether to generate a "test" or a "summary".
     - `--file-type` (`-f`): Specify the file type (`pdf` or `pptx`).

6. **View Output**:
   Access the generated HTML files in the `output/` directory using your preferred web browser.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

For more information and to access the source code, visit the [LLMTestForge GitHub repository](https://github.com/yuvalakavian/LLMTestForge).

