from django.shortcuts import render


def upload_pdf(request):
    if request.method == 'POST' and request.FILES['pdf_file']:
        pdf_file = request.FILES['pdf_file']
        # Here you can add code to process the uploaded PDF file
        return render(request, 'scanner/upload_success.html')
    return render(request, 'scanner/upload_pdf.html')
