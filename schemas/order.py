from pydantic import BaseModel, Field, validator
from datetime import date

class OrderModel(BaseModel):
    product_name: str = Field(..., min_length=1)
    quantity: int = Field(default=1, gt=0)
    price_per_unit: float = Field(default=1, gt=0)
    creation_date: date = Field(default=date.today)

    @validator('product_name')
    def validate_product_name(cls, value):
        if not value.strip():
            raise ValueError("Name of product cannot be empty")
        return value

    @validator('creation_date')
    def validate_creation_date(cls, value):
        if value > date.today():
            raise ValueError("Date of creating product cannot be in the future")
        return value
