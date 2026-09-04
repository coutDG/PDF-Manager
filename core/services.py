# upload document
# upload -> to pdf -> thumbnail -> folder with same name as pdf file -> images
# total pages
# upload_date -> datetime
from datetime import datetime
from db.repository import DocumentRepository
from core.file_manager import FileManager
from core.thumbnail import ThumbnailGenerator
from core.reader import PDFReader
from core.models import Document
import os

PDF_STORAGE = os.path.join('storage','pdf')

class DocumentService:
    def __init__(self):
        self.repo = DocumentRepository()
        self.file_manager = FileManager()
        self.thumbnail_generator = ThumbnailGenerator()
        self.reader= PDFReader()
    def upload_document(self,uploaded_file,tags,description,lecture_date = None):
        
        file_path = self.file_manager.save_file(uploaded_file,tags,description,lecture_date)

        #generate thumbnail
        thumbnail_path = self.thumbnail_generator.generate_thumbail(file_path)
        #get total pages
        total_pages = self.thumbnail_generator.get_total_pages(file_path)
        #convert to images
        image_paths = self.reader.convert_pdf_to_images(file_path)
        #required variables : upload_date

        doc = Document(
            id = None,
            name = uploaded_file.name,
            path=file_path,
            thumbnail_path = thumbnail_path,
            tags = tags,
            description = description,
            upload_date = datetime.now().strftime("%Y-%m-%d"),
            lecture_date = lecture_date,
            total_pages = total_pages
        )
        #save to database
        self.repo.add_document(doc)
        #self.repo.add_document(doc)
    
    def search_documents(self,tag = None, date = None):
            return self.repo.search_document(tag,date)


    def get_all_document(self):
         return self.repo.get_all_document()



