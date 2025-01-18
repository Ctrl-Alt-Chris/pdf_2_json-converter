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
        print(f"An error occurred with file {file_path}: {e}")

def process_all_pdfs_in_folder(folder_path):
    """
    Process all PDF files in a given folder and convert them to JSON.
    
    :param folder_path: Path to the folder containing PDF files.
    :return: None
    """
    # Ensure the folder exists
    if not os.path.isdir(folder_path):
        print(f"Folder does not exist: {folder_path}")
        return
    
    # Get a list of all PDF files in the folder
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
    
    if not pdf_files:
        print(f"No PDF files found in folder: {folder_path}")
        return
    
    # Process each PDF file
    for pdf_file in pdf_files:
        input_pdf = os.path.join(folder_path, pdf_file)
        output_json = os.path.join(folder_path, os.path.splitext(pdf_file)[0] + '.json')
        pdf_to_json(input_pdf, output_json)

# Example usage
if __name__ == "__main__":
    folder_path = r"C:\Users\chris\Documents\pdfs"  # Replace <YourUsername>
    process_all_pdfs_in_folder(folder_path)
