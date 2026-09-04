from datetime import datetime
import os

PDF_STORAGE = os.path.join('storage','pdf')

class FileManager:
   
    def save_file(self,uploaded_file,tags,description,lecture_date = None):
        doc = []
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{timestamp}_{uploaded_file.name}"
        
        file_path = os.path.join(PDF_STORAGE,filename)
        #save file
        with open(file_path,'wb') as f:
            f.write(uploaded_file.read())
            
        return file_path
