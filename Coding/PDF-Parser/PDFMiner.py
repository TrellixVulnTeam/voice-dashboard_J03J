from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter, XMLConverter, HTMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import BytesIO
from bs4 import BeautifulSoup as bs

def convert_pdf(path, format='text', codec='utf-8', password=''):
    rsrcmgr = PDFResourceManager()
    retstr = BytesIO()
    laparams = LAParams()
    if format == 'text':
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    elif format == 'html':
        device = HTMLConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    elif format == 'xml':
        device = XMLConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    else:
        raise ValueError('provide format, either text, html or xml!')
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue().decode()
    soup = bs(text)
    prettyHTML = soup.prettify()
    print(prettyHTML)
    # html_file = open("../../Data/document-page0.xml", "w")
    # html_file.write(prettyHTML)
    # html_file.close()
    # fp.close()
    # device.close()
    # retstr.close()
    return text

def main():
    convert_pdf('../../Data/20180316 Lagebericht_DE/page_3.pdf', format='text')
    print ('Done!')

if __name__ == '__main__':
    main()