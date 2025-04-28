from pydantic import BaseModel, Field, validator
from typing import Optional
from bson import ObjectId
class Project(BaseModel):
    # The id when you do an insert, but when you do a get project or data, it will be there
    id: Optional[ObjectId] = Field(None, alias="_id")
    project_id: str = Field(..., min_length=1)
    #cls يعبر عن  الكلاس نفسه
    # وcls هو اختصار لـ classmethod

    @validator('project_id')
    def validate_project_id(cls, value):
        if not value.isalnum():
            raise ValueError('project_id must be alphanumeric')
        
        return value
    #لو بقيت حاجة غريبة عنك ك بايثون متتصرفشي معاه زي objectid
    # لو عايز تتصرف معاه ك string او int او float او غيره
    class Config:
        arbitrary_types_allowed = True