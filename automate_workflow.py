import argparse
import subprocess
import sys
import os

def run_generate_json(generate_type, file_type, input_file, custom_prompt):
    """Runs generate_json.py with the specified arguments."""
    # Build the base command
    cmd = ['python', 'scripts/generate_json.py', '-g', generate_type, '-f', file_type, '-i', input_file]
    
    # If a custom prompt is provided, add it to the command
    if custom_prompt:
        cmd.extend(['-c', custom_prompt])
    
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running generate_json.py: {e}")
        sys.exit(1)

def determine_html_script(generate_type):
    """Determines which HTML generation script to use based on the generate_type argument."""
    if generate_type == "test":
        return "scripts/generate_test_html_from_json.py"
    elif generate_type == "summary":
        return "scripts/generate_summary_html_from_json.py"
    else:
        print("Error: Invalid generate_type. Must be 'test' or 'summary'.")
        sys.exit(1)

def run_html_generation(html_script, json_file, output_file):
    """Runs the selected HTML generation script with the JSON input and HTML output."""
    try:
        subprocess.run(
            ['python', html_script, '--input-file', json_file, '--output-file', output_file],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error running {html_script}: {e}")
        sys.exit(1)

def parse_arguments():
    """Parses command-line arguments for the automation script."""
    parser = argparse.ArgumentParser(description="Automate JSON and HTML generation from PDF/PPTX files.")
    
    parser.add_argument(
        "--generate-type", "-g",
        choices=["test", "summary"],
        required=True,
        help="Specify whether to generate a 'test' or a 'summary'."
    )
    
    parser.add_argument(
        "--file-type", "-f",
        choices=["pdf", "pptx"],
        required=True,
        help="Specify the file type (pdf or pptx)."
    )

    parser.add_argument(
        "--input-file", "-i",
        required=True,
        help="Path to the input PDF or PPTX file."
    )
    
    parser.add_argument(
        "--custom-prompt", "-c",
        help="Optional custom prompt to override the default prompt instructions."
    )
    
    return parser.parse_args()

def main():
    args = parse_arguments()
    generate_type = args.generate_type
    file_type = args.file_type
    input_file = args.input_file
    custom_prompt = args.custom_prompt

    # Generate output filenames based on input file and output folder
    output_json = "output/response.json"
    output_file = os.path.join("output", os.path.splitext(os.path.basename(input_file))[0] + ".html")

    print(f"Processing {input_file} as {generate_type} ({file_type})...")
    if custom_prompt:
        print(f"Custom prompt provided: {custom_prompt}")
    
    run_generate_json(generate_type, file_type, input_file, custom_prompt)
    
    html_script = determine_html_script(generate_type)
    
    run_html_generation(html_script, output_json, output_file)

    print(f"HTML generation complete. Output saved to {output_file}")

if __name__ == "__main__":
    main()
