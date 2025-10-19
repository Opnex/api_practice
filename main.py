# # from fastapi import FastAPI
# # from pydantic import BaseModel

# # app = FastAPI()

# # # Data model
# # class User(BaseModel):
# #     name: str
# #     age: int

# # # Routes
# # @app.get("/")
# # def home():
# #     return {"message": "Welcome to FastAPI"}

# # @app.post("/users")
# # def create_user(user: User):
# #     return {"message": f"User {user.name} (age {user.age}) created successfully!"}


# from fastapi import FastAPI
# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Message": f"Hello, FastAPI"}