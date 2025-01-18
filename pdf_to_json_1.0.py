import PyPDF2
import json
import os

def pdf_to_json(file_path, output_json_path):
    """
    Convert a PDF file to text and save it as a JSON file.
    
    :param file_path: Path to the PDF file.
    :param output_json_path: Path to save the output JSON file.
    :return: None
    """
    try:
        # Open the PDF file
        with open(file_path, 'rb') as pdf_file:
            # Create a PDF reader object
            reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            
            # Iterate through all the pages and extract text
            for page in reader.pages:
                text += page.extract_text() + "\n"
            
            # Split text into paragraphs
            paragraphs = text.split("\n\n")
            
            # Prepare JSON structure
            data = {
                "file_name": os.path.basename(file_path),
                "content": paragraphs
            }
            
            # Save the JSON to the specified output file
            with open(output_json_path, 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=4)
        
        print(f"JSON file saved to: {output_json_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    input_pdf = r"C:\Users\chris\Documents\pdfs\mock_example.pdf"  # Replace <YourUsername>
    output_json = r"C:\Users\chris\Documents\pdfs\example.json"
    pdf_to_json(input_pdf, output_json)
