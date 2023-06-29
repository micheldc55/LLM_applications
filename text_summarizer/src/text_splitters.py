import PyPDF2

def read_pdf_chunks(file_path, chunk_size=1000, overlap=100):
    with open(file_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        num_pages = len(reader.pages)
        text = ''
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
        chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size-overlap)]
        del text
        yield chunks

if __name__ == "__main__":
    chunks = read_pdf_chunks("/workspace/data/Price Optimization for Revenue Maximization at Scale.pdf", 
                             chunk_size=2500, overlap=1000)
    
    for chunk in chunks:
        print(chunk)
        break