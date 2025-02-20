import json
import ast
import re

def format_list_to_html(lst):
    """Recursively formats a list into nested HTML lists."""
    html = "<ul>"
    for item in lst:
        html += f"<li>{format_value(item)}</li>"
    html += "</ul>"
    return html

def format_dict_to_html(data):
    """Recursively formats dictionaries into nested HTML lists."""
    html = "<ul>"
    for key, value in data.items():
        html += f"<li><strong>{key}:</strong> {format_value(value)}</li>"
    html += "</ul>"
    return html

def format_numbered_string(value):
    """
    If the string contains a numbered list pattern (e.g., "1. ... 2. ..."),
    split the string and return an HTML fragment with a paragraph for any text
    before the list and a proper HTML list for the numbered items.
    """
    # Split by pattern where a number followed by a dot and space starts a new item
    items = re.split(r'\s*(?=\d+\.\s)', value.strip())
    # If there is only one part, then nothing special to do.
    if len(items) <= 1:
        return value
    html = ""
    # If the first item does not start with a number, assume it's introductory text.
    if not re.match(r'\d+\.\s', items[0]):
        html += f"<p>{items[0]}</p>"
        items = items[1:]
    html += "<ul>" + "".join(f"<li>{item}</li>" for item in items if item != '') + "</ul>"
    return html

def format_value(value):
    """Returns an HTML representation of the value."""
    if isinstance(value, dict):
        return format_dict_to_html(value)
    elif isinstance(value, list):
        return format_list_to_html(value)
    elif isinstance(value, str):
        # Check if the string appears to contain a numbered list pattern.
        if re.search(r'\d+\.\s', value):
            return format_numbered_string(value)
        # Attempt to parse the string as a literal list (if it looks like one)
        stripped = value.strip()
        if stripped.startswith('[') and stripped.endswith(']'):
            try:
                parsed = ast.literal_eval(stripped)
                if isinstance(parsed, list):
                    return format_list_to_html(parsed)
            except Exception:
                pass
        return value
    else:
        return str(value)

def json_to_html(json_data, output_file="output/summary.html"):
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
            body { 
                font-family: Arial, sans-serif; 
                margin: 40px; 
                background: linear-gradient(120deg, #3a3d40, #5c5e60); 
                color: #eee; 
            }
            h2 { 
                color: #ffffff; 
                background: #2c3e50; 
                padding: 12px; 
                border-radius: 5px; 
                text-transform: uppercase; 
                letter-spacing: 1px; 
            }
            p { 
                font-size: 16px; 
                line-height: 1.5; 
            }
            pre { 
                background: #2d2d2d; 
                color: #f8f8f8; 
                padding: 12px; 
                border-radius: 5px; 
                overflow-x: auto; 
            }
            ul { 
                list-style-type: disc; 
                padding-left: 20px; 
            }
            li { 
                background: #444; 
                color: #ddd; 
                margin: 5px 0; 
                padding: 10px; 
                border-radius: 5px; 
                font-weight: bold; 
            }
            .container { 
                max-width: 900px; 
                margin: auto; 
                background: #3b3b3b; 
                padding: 20px; 
                border-radius: 10px; 
                box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.3); 
            }
        </style>
    </head>
    <body>
        <div class="container">
    """
    
    for key, value in json_data.items():
        html_content += f"<h2>{key}</h2>"
        formatted_value = format_value(value)
        # If the formatted value is an HTML list, render it as is; otherwise wrap in a paragraph.
        if formatted_value.strip().startswith("<ul>"):
            html_content += formatted_value
        else:
            html_content += f"<p>{formatted_value}</p>"
    
    html_content += "</div></body></html>"
    
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(html_content)
    
    print(f"HTML file '{output_file}' generated successfully.")

if __name__ == "__main__":
    with open("output/response.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    json_to_html(data)
