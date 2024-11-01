from pydantic import BaseModel

class FileUpload(BaseModel):
    path: str
    
class FileCreate(BaseModel):
    name: str
    path: str
    size: int
    
