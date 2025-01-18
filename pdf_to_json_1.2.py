# pdf_to_json
#version 1.2
# detects current directory location of where script is placed



import os
import json
from PyPDF2 import PdfReader  

# Example library for reading PDFs
from datetime import datetime

def pdf_to_json(pdf_path, json_path):
    # Example function to convert PDF to JSON
    reader = PdfReader(pdf_path)
    content = {"pages": [page.extract_text() for page in reader.pages]}
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(content, json_file, ensure_ascii=False, indent=4)

# Get the current script directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# List all PDF files in the directory
pdf_files = [file for file in os.listdir(current_directory) if file.lower().endswith('.pdf')]

if not pdf_files:
    print("No PDF files detected in the current directory.")
else:
    print("The following PDF files were detected for conversion:")
    for file in pdf_files:
        print(f"- {file}")

    user_input = input("Do you want to proceed with the conversion? (yes/no): ").strip().lower()

    if user_input == 'yes':
        report_file = os.path.join(current_directory, "report_pdf_convert_done.txt")
        with open(report_file, 'a', encoding='utf-8') as report:
            for file_name in pdf_files:
                pdf_path = os.path.join(current_directory, file_name)
                json_path = os.path.join(current_directory, f"{os.path.splitext(file_name)[0]}.json")
                
                print(f"Converting {file_name} to JSON...")
                pdf_to_json(pdf_path, json_path)
                # Append the result to the report file
                report.write(f"{datetime.now()}: Converted {file_name} to {os.path.basename(json_path)}\n")
        
        print("Task done boss")
        input("Press OK to close the command window.")
    else:
        print("Conversion canceled.")
