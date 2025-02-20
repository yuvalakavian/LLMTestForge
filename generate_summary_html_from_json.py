import json

def format_dict_to_html(data):
    """Recursively formats dictionaries into nested HTML lists."""
    html = "<ul>"
    for key, value in data.items():
        html += f"<li><strong>{key}:</strong> "
        if isinstance(value, dict):
            html += format_dict_to_html(value)
        elif isinstance(value, list):
            html += "<ul>" + "".join(f"<li>{format_dict_to_html(item) if isinstance(item, dict) else item}</li>" for item in value) + "</ul>"
        else:
            html += f"{value}"
        html += "</li>"
    html += "</ul>"
    return html

def json_to_html(json_data, output_file="output.html"):
    if not isinstance(json_data, dict):
        raise ValueError("Input data must be a dictionary")
    
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>JSON to HTML</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: linear-gradient(120deg, #3a3d40, #5c5e60); color: #eee; }
            h2 { color: #ffffff; background: #2c3e50; padding: 12px; border-radius: 5px; text-transform: uppercase; letter-spacing: 1px; }
            pre { background: #2d2d2d; color: #f8f8f8; padding: 12px; border-radius: 5px; overflow-x: auto; }
            ul { list-style-type: disc; padding-left: 20px; }
            li { background: #444; color: #ddd; margin: 5px 0; padding: 10px; border-radius: 5px; font-weight: bold; }
            .container { max-width: 900px; margin: auto; background: #3b3b3b; padding: 20px; border-radius: 10px; box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.3); }
        </style>
    </head>
    <body>
        <div class="container">
    """
    
    for key, value in json_data.items():
        html_content += f"<h2>{key}</h2>"
        html_content += format_dict_to_html(value) if isinstance(value, dict) else f"<p>{value}</p>"
    
    html_content += "</div></body></html>"
    
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(html_content)
    
    print(f"HTML file '{output_file}' generated successfully.")


if __name__ == "__main__":
    with open("response.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    json_to_html(data)
