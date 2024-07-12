from pydantic import BaseModel
from typing import List, Dict


class DataModel(BaseModel):
    id: int
    name: str
    region: str
    additional_info: Dict[str, str]


class DataCollectionResponse(BaseModel):
    status: str
    country: str
    data: List[DataModel]
