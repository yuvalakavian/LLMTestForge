import argparse
import json
import random

# Function to generate HTML
def generate_html(data):
    html_content = """
    <!DOCTYPE html>
    <html lang="he">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>מבחן</title>
        <link href="https://fonts.googleapis.com/css2?family=Assistant:wght@400;600&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Assistant', sans-serif;
                direction: rtl;
                margin: 0;
                padding: 0;
                background-color: #faf7fc;
                color: #2c3e50;
            }
            .container {
                max-width: 900px;
                margin: 40px auto;
                padding: 40px;
                background-color: #f6edf9;
                border-radius: 16px;
                box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08);
            }
            h1, h2 {
                text-align: center;
                margin-bottom: 30px;
                color: #8c4ca8;
            }
            .question, .open-question {
                color: #8c4ca8;
                margin-bottom: 35px;
                padding: 24px;
                background-color: #F5F3F7;
                border-radius: 12px;
                border-right: 6px solid #4929B9;
                box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
            }
            .question p, .open-question p {
                font-size: 18px;
                margin: 10px 0;
            }
            .options p {
                margin: 8px 0;
                padding: 10px 14px;
                background-color: #FFFFFF;
                border-radius: 8px;
                transition: background-color 0.3s;
            }
            .options p:hover {
                background-color: #dce3e8;
            }
            .answer, .answer-text {
                font-weight: 600;
                color: #8c4ca8;
                margin-top: 18px;
                display: none;
            }
            .show-answer-btn {
                margin-top: 15px;
                padding: 10px 20px;
                background-color: #4929B9;
                color: #fff;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }
            .show-answer-btn:hover {
                background-color: #8c4ca8;
            }
        </style>

        <script>
            function toggleAnswer(id) {
                var answer = document.getElementById(id);
                answer.style.display = (answer.style.display === "none" || answer.style.display === "") ? "block" : "none";
            }
        </script>
    </head>
    <body>
        <div class="container">
            <h1>מבחן</h1>
            <h2>שאלות רב-ברירה</h2>
    """
    
    # Add multiple choice questions with shuffled options
    for index, question in enumerate(data['exam']['multiple_choice']):
        options = question['options'].copy()
        random.shuffle(options)
        html_content += f"""
        <div class="question">
            <p>{question['question']}</p>
            <div class="options">
        """
        for option in options:
            html_content += f"<p>{option}</p>"
        
        html_content += f"""
            </div>
            <button class="show-answer-btn" onclick="toggleAnswer('answer{index}')">הצג תשובה</button>
            <p id="answer{index}" class="answer">תשובה נכונה: {question['answer']}</p>
        </div>
        """
    
    html_content += """
            <h2>שאלות פתוחות</h2>
    """
    
    # Add open-ended questions
    for index, question in enumerate(data['exam']['open_questions']):
        html_content += f"""
        <div class="open-question">
            <p>{question['question']}</p>
            <button class="show-answer-btn" onclick="toggleAnswer('open-answer{index}')">הצג תשובה</button>
            <p id="open-answer{index}" class="answer-text">{question['answer']}</p>
        </div>
        """
    
    html_content += """
        </div>
    </body>
    </html>
    """
    
    return html_content

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Generate HTML for an exam from a JSON file.")
    
    parser.add_argument(
        "--input-file", "-i",
        required=True,
        help="Path to the input JSON file containing the exam data."
    )
    
    parser.add_argument(
        "--output-file", "-o",
        default="output/exam.html",
        help="Path to the output HTML file (default: 'output/exam.html')."
    )

    return parser.parse_args()

def main():
    # Parse command-line arguments
    args = parse_arguments()

    # Read the input JSON file
    with open(args.input_file, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    # Generate the HTML
    html_output = generate_html(data)

    # Save the output to a file
    with open(args.output_file, 'w', encoding='utf-8') as f:
        f.write(html_output)

    print(f"HTML file generated successfully: {args.output_file}")

if __name__ == "__main__":
    main()
