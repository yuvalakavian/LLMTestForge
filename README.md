# LLMTestForge

LLMTestForge is an advanced testing framework that leverages AI to transform documents into structured data and human-readable reports. It uses ChatGPT to parse PDF and PPTX files, extract their content, and convert the text into structured JSON format. Then, it generates HTML reports from that JSON data.

## Features

- **PDF/PPTX to JSON Conversion**: Uses ChatGPT to extract text from PDF and PPTX files, creating structured JSON data.
- **JSON to HTML Conversion**: Generates human-readable HTML reports from the JSON data, making it easy to visualize the parsed content.
- **Automation**: Full workflow automation through a single script for converting files and generating reports.

## How It Works

1. **Text Extraction**: The framework processes PDF or PPTX files, extracting their text content.
2. **AI Processing**: ChatGPT analyzes the extracted text, organizing it into a structured JSON format.
3. **HTML Generation**: The structured JSON is then converted into a customized HTML report, either for a summary or a test result.

## Workflow

You can automate the entire process (from file conversion to report generation) using the `automate_workflow.py` script.

### Usage

Run the following command to automate the entire workflow:

```bash
python automate_workflow.py --generate-type <test|summary> --file-type <pdf|pptx> --input-file <input_file_path>
```

- `--generate-type` (`-g`): Choose `test` for test results or `summary` for a content summary.
- `--file-type` (`-f`): Specify the input file type (`pdf` or `pptx`).
- `--input-file` (`-i`): Path to the input PDF or PPTX file.

The script generates:
1. A JSON file in the `output/` folder.
2. An HTML file summarizing or testing the extracted data, saved in the same folder.

### Example

```bash
python automate_workflow.py -g summary -f pdf -i input/test/example.pdf
```

This command processes `example.pdf`, creates `example.json` in `output/`, and then generates `example.html` summarizing the extracted data.
![image](https://github.com/user-attachments/assets/bdd872f0-0bdb-4f3d-8b25-b42318415429)




## Contributing

Contributions are welcome! Fork the repo, make your changes, and submit a pull request to enhance the framework.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
