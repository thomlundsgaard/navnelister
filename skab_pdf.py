import pdfkit;
options = {
    'orientation': 'landscape',
}
pdfkit.from_file('test.html','test.pdf', options=options);

