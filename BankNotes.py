
from pydantic import BaseModel

## class to define the structure of the input data
class BankNote(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float