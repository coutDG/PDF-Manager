# upload document
# upload -> to pdf -> thumbnail -> folder with same name as pdf file -> images
# total pages
# upload_date -> datetime
from db.repository import DocumentRepository
from core.file_manager import FileManager
from core.thumbnail import ThumbnailGenerator
import os

PDF_STORAGE = os.path.join('storage','pdf')

class DocumentService:
    def __init__(self):
        self.repo = DocumentRepository
        self.file_manager = FileManager()
        self.thumbnail_generator = ThumbnailGenerator()

    def upload_document(self,uploaded_file,tags,description,lecture_date = None):
        doc = []
        
        file_path = self.file_manager.save_file(uploaded_file,tags,description,lecture_date)

        #generate thumbnail
        thumbail_path = self.thumbnail_generator.generate_thumbail(file_path)
        #get total pages
        total_pages = self.thumbnail_generator.get_total_pages(file_path)
        #convert to images

        #required variables : upload_date
        #save to database
        #self.repo.add_document(doc)




