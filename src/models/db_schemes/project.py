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
        
    @classmethod
    def get_indexes(cls):

        return [
            {
                "key": [
                    ("project_id", 1)
                ],
                "name": "project_id_index_1",
                  #قيمة unique بتعبر عن ان الحقل ده فريد ولا لأ
                #هنا لا يوجد p[roject_id] بنفس القيمة
                #يعني مفيش اتنين project بنفس ال project id
            
                "unique": True
            }
        ]