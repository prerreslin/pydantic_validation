from pydantic import EmailStr,BaseModel, Field
from .order import OrderModel

class UserModel(BaseModel):
    name: str = Field(...,min_length=3)
    email: EmailStr

    @validator('name')
    def validate_user_name(cls, value):
        if not value.strip():
            raise ValueError("Name of user cannot be empty")
        return value