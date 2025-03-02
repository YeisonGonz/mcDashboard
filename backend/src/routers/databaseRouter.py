from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
import hashlib
from src.auth.jwtAuth import create_access_token
from src.database.DatabaseConnector import DatabaseConnector
from src.database.ORM import ORM
from src.models.User import IncomingUser

router = APIRouter()


@router.get("/api/database", tags=["database"])
async def get_database():
    try:
        DatabaseConnector().get_instance()
    except FileNotFoundError:
        return HTTPException(status_code=500, detail="Failed to connect")
    

@router.post("/api/user")
async def insert_user(incoming_user: IncomingUser):
    try:
        ORM_BASE = ORM(DatabaseConnector.get_instance())

        encoded_password = incoming_user.password.encode('utf-8')
        hash_object = hashlib.sha256(encoded_password)
        hash_password = hash_object.hexdigest()

        if not ORM_BASE.insert_dashboardUser(incoming_user.name, hash_password):
            return HTTPException(status_code=500, detail="That user already exists")
        
        return {"message": "Action completed"}
    except FileNotFoundError:
        return HTTPException(status_code=500, detail="Failed to connect")
    


@router.post("/api/login")
async def login(incoming_user: IncomingUser):
    try:
        ORM_BASE = ORM(DatabaseConnector.get_instance())

        if not ORM_BASE.verify_password(incoming_user.name, incoming_user.password):
            raise HTTPException(status_code=401, detail="Incorrect username or password")
        
        access_token = create_access_token(data={"sub": incoming_user.name})
        
        return {"access_token": access_token, "token_type": "bearer"}
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Failed to connect to database")
