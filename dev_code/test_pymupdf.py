"""
PyMuPdf
"""
import fitz

# Open pdf file
doc = fitz.open("test.pdf")

# Check if pdf is password protected
if doc.needsPass:
    password = ""
    doc.authenticate(password)

# Read pages
for i in range(doc.page_count):
    page = doc.load_page(i)
    text = page.getText("text")
    print(text)
    break
