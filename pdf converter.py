import PyPDF2

def pdf_to_text(pdf_path, text_path):
    try:
        with open(pdf_path, 'rb') as pdf_file:
            reader=PyPDF2.PdfReader(pdf_file)
            text=''
            for page_num in range(len(reader.pages)):
                page = reader.pages [page_num]
                text += page.extract_text() # Updated method name
                
        with open(text_path, 'w') as text_file :
            text_file.write(text)
        print(f"Text has been successfully extracted and saved to {text_path}")

    except FileNotFoundError:
            print(" file is not found")
    except Exception as e:
         print(f"An error occurred: {e}")
if __name__ ==  "__main__":
    pdf_path= input("Enter the path to the PDF file: ")
    text_path=input("Enter the path to save the text file: ")
    print(f"Text has been successfully extracted and saved to {text_path}")
    pdf_to_text(pdf_path, text_path)