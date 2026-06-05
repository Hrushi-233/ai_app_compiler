from pydantic import BaseModel
from typing import List

class DesignSchema(BaseModel):
    entities: List[str]
    flows: List[str]