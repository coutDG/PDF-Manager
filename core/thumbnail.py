import os
import pymupdf
THUMBNAIL_DIR = os.path.join('storage','thumbnails')


class ThumbnailGenerator:

    def generate_thumbail(self,pdf_path):
        doc = pymupdf.open(pdf_path) #open the pdf
        page = doc.load_page(0) #get first page
        pix = page.get_pixmap() #sinngle first page pixel map
        base_name = os.path.basename(pdf_path).replace('.pdf','.png') #change the extension
        thumb_path = os.path.join(THUMBNAIL_DIR,base_name)
        pix.save(thumb_path)
        doc.close()
        return thumb_path
    
    def get_total_pages(self,pdf_path):
        doc = pymupdf.open(pdf_path)
        total = len(doc)
        doc.close()
        return total
