import subprocess
import sys
import os

def run_generate_json(generate_type, file_type, input_file, output_json):
    """Runs generate_json.py with the specified arguments."""
    try:
        subprocess.run(
            ['python', 'generate_json.py', '-g', generate_type, '-f', file_type, input_file, output_json],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error running generate_json.py: {e}")
        sys.exit(1)

def determine_html_script(generate_type):
    """Determines which HTML generation script to use based on the generate_type argument."""
    if generate_type == "test":
        return "generate_test_html_from_json.py"
    elif generate_type == "summary":
        return "generate_summary_html_from_json.py"
    else:
        print("Error: Invalid generate_type. Must be 'test' or 'summary'.")
        sys.exit(1)

def run_html_generation(html_script, json_file, output_html):
    """Runs the selected HTML generation script with the JSON input and HTML output."""
    try:
        subprocess.run(
            ['python', html_script, json_file, output_html],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error running {html_script}: {e}")
        sys.exit(1)

def main(generate_type, file_type, input_file):
    if file_type not in ["pdf", "pptx"]:
        print("Error: file_type must be 'pdf' or 'pptx'.")
        sys.exit(1)

    output_json = os.path.splitext(input_file)[0] + ".json"
    output_html = os.path.splitext(input_file)[0] + ".html"

    run_generate_json(generate_type, file_type, input_file, output_json)
    html_script = determine_html_script(generate_type)
    run_html_generation(html_script, output_json, output_html)

    print(f"HTML generation complete. Output saved to {output_html}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python automate_workflow.py <generate-type> <file-type> <input_file>")
        sys.exit(1)

    generate_type = sys.argv[1]
    file_type = sys.argv[2]
    input_file = sys.argv[3]

    main(generate_type, file_type, input_file)
