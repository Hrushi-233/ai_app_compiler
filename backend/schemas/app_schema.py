from pydantic import BaseModel
from typing import List, Dict

class UISchema(BaseModel):
    pages: List[Dict]

class APISchema(BaseModel):
    endpoints: List[Dict]

class DBSchema(BaseModel):
    tables: List[Dict]

class AuthSchema(BaseModel):
    roles: List[Dict]