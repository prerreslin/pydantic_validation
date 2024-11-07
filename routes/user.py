from main import app
from db import User,Session,Order
from schemas import UserModel,OrderModel
from fastapi import HTTPException
from pydantic import EmailStr

@app.post("/create_user")
def create_user(data:UserModel,order_data:OrderModel):
    with Session() as session:
        user = session.query(User).where(User.email == data.email).first()
        if user:
            raise HTTPException(status_code=400, detail="Email already exists")
        
        new_user = User(
            name=data.name,
            email=data.email
        )
        session.add(new_user)
        session.commit()
        session.refresh(new_user)

        new_order = Order(
            product_name=order_data.product_name,
            quantity=order_data.quantity,
            price_per_unit=order_data.price_per_unit,
            user_id=new_user.id
        )
        session.add(new_order)
        session.commit()
        session.refresh(new_order)

        return {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email
        }


@app.get("/get_user")
def get_user(email:EmailStr):
    with Session() as session:
        user = session.query(User).where(User.email == email).first()
        if not user:
            raise HTTPException(status_code=404,detail="User not found")
        return user
