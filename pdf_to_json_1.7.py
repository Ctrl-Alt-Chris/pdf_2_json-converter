import os
import json
import time
from PyPDF2 import PdfReader  # Example library for reading PDFs
from datetime import datetime

def pdf_to_json(pdf_path, json_path):
    # Example function to convert PDF to JSON
    reader = PdfReader(pdf_path)
    content = {"pages": [page.extract_text() for page in reader.pages]}
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(content, json_file, ensure_ascii=False, indent=4)

def get_user_confirmation():
    while True:
        user_input = input("Do you want to proceed with the conversion? (y/n): ").strip().lower()
        if user_input in ['y', 'yes', 'ok']:
            return True
        elif user_input in ['n', 'no']:
            print("OK, see you later!")
            time.sleep(2)
            exit()
        else:
            print("I didn't quite get that. Can you please enter 'y' for yes and 'n' for no?")

def post_conversion_options():
    while True:
        user_input = input("Press 'c' to close or 'r' to run again: ").strip().lower()
        if user_input == 'c':
            print("OK, see you later!")
            time.sleep(2)
            exit()
        elif user_input == 'r':
            print("OK, on it!")
            return
        else:
            print("Invalid input. Please press 'c' to close or 'r' to run again.")

def main():
    # Get the current script directory
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # List all PDF files in the directory
    pdf_files = [file for file in os.listdir(current_directory) if file.lower().endswith('.pdf')]

    if not pdf_files:
        print("Hey, I looked all over, I don't see any PDFs in this directory.")
    else:
        print("Hey Boss, I found these files below to convert:")
        for file in pdf_files:
            print(f"- {file}")

        if get_user_confirmation():
            report_file = os.path.join(current_directory, "report_pdf_convert_done.txt")
            with open(report_file, 'a', encoding='utf-8') as report:
                for file_name in pdf_files:
                    pdf_path = os.path.join(current_directory, file_name)
                    json_path = os.path.join(current_directory, f"{os.path.splitext(file_name)[0]}.json")
                    
                    print(f"Converting {file_name} to JSON...")
                    try:
                        pdf_to_json(pdf_path, json_path)
                        # Append the result to the report file
                        report.write(f"{datetime.now()}: Converted {file_name} to {os.path.basename(json_path)}\n")
                    except Exception as e:
                        print(f"Error converting {file_name}: {e}")
                        report.write(f"{datetime.now()}: Failed to convert {file_name}. Error: {e}\n")
            
            print("Task done boss")
            post_conversion_options()
        else:
            print("Conversion canceled.")

if __name__ == "__main__":
    while True:
        main()
