from pydantic import BaseModel
from typing import List

class IrisRequest(BaseModel):
    X: List[List[float]]

class IrisResponse(BaseModel):
    y: List[int]
