# pdf_2_json-converter
Command line interface controlled pdf to json converter
# PDF to JSON Converter - README

## Project Overview
This Python script converts PDF files to JSON format. It dynamically processes files in the same directory as the script, eliminating the need to hard-code folder paths. The script also includes user-friendly prompts, error handling, and a detailed report of processed files.

---

## Features
1. **Dynamic File Detection**:
   - Automatically detects PDF files in the same directory as the script.
   - Processes only those files without requiring folder path hard-coding.

2. **User Interaction**:
   - Lists detected files for conversion.
   - Prompts the user for confirmation before proceeding.
   - Accepts multiple forms of confirmation (e.g., `y`, `yes`, `ok` for "yes" and `n`, `no` for "no").
   - Gracefully handles invalid inputs with helpful error messages.

3. **Error Handling**:
   - Logs errors during PDF conversion without terminating the script.
   - Errors are recorded in the report file for future reference.

4. **Report Generation**:
   - Creates or appends to a `report_pdf_convert_done.txt` file.
   - Logs each conversion with a timestamp.

5. **Completion Feedback**:
   - Displays a message (`Task done boss`) upon successful completion.
   - Waits for user input (`Press OK to close the command window`) before closing.

---

## Version History

### **Version 1.0**
- Basic functionality to convert PDF files to JSON.
- Hard-coded folder path for file processing.

### **Version 1.1**
- Removed hard-coded folder dependency.
- Dynamically processes files in the same directory as the script.

### **Version 1.2**
- Added user prompt to list detected files.
- Implemented a yes/no confirmation before starting the conversion process.
- Added completion message (`Task done boss`) and user prompt to close the command window.

### **Version 1.3**
- Integrated logging functionality to create a `report_pdf_convert_done.txt` file.
  - Appends to the report if it already exists, rather than overwriting.
- Included timestamps in the report for each file processed.

### **Version 1.4**
- Enhanced user input handling:
  - Accepts `y`, `yes`, `ok` for "yes" and `n`, `no` for "no".
  - Displays error message for invalid inputs and re-prompts user.

### **Version 1.5**
- Improved user messages for file detection:
  - If no PDFs are found: `Hey, I looked all over, I don't see any PDFs in this directory.`
  - If PDFs are found: `Hey Boss, I found these files below to convert:`
- Added error handling during conversion to log any issues with specific files.

### **Version 1.6**
- Closing script close or rerun commands added
- The script now provides an option to press 'c' to close or 'r' to run again at the end.
- error handling invalid inputs, prompting the user to try again until they provide valid input.
- Exiting the script with a message if 'c' is pressed.
- The main loop keeps the program running if 'r' is pressed.

### **Version 1.7**
- Fixed loop if user elects to not run conversion
- When the user responds 'n' to the conversion confirmation, the script prints "OK, see you later!" and exits after a 2-second pause.
- This ensures the exit message is consistent whether the user cancels the conversion or chooses to close the script after the task is done.


---

## How to Use
1. Place the script in the directory containing your PDF files.
2. Run the script.
3. Follow the prompts:
   - Confirm whether you want to proceed with the conversion.
   - Wait for the script to complete and check the message (`Task done boss`).
   - Press OK to close the window.
4. Review the `report_pdf_convert_done.txt` file for a summary of processed files.

---

## Requirements
- Python 3.x
- `PyPDF2` library
  
Install `PyPDF2` using pip:
```bash
pip install PyPDF2
```

---
