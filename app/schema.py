from pydantic import BaseModel

class CustomerData(BaseModel):
    age: int
    balance: float
    products: int
    active: int
