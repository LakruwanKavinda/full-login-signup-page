from django.shortcuts import render
from .forms import UploadFileForm
import PyPDF2


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = request.FILES['file']
            pdf_text = extract_text_from_pdf(pdf_file)
            return render(request, 'pdf_reader/result.html', {'pdf_text': pdf_text})
    else:
        form = UploadFileForm()
    return render(request, 'pdf_reader/upload.html', {'form': form})


def extract_text_from_pdf(pdf_file):
    text = ''
    try:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
    except Exception as e:
        text = f'Error extracting text: {str(e)}'
    return text
