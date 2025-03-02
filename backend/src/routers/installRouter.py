from fastapi import APIRouter
from loguru import logger 
from src.database.DatabaseConnector import DatabaseConnector
from src.database.ORM import ORM


try:
    ORM_BASE = ORM(DatabaseConnector.get_instance())
except FileNotFoundError:
    logger.warning("The database does not exist, the installation starts.")
    DatabaseConnector().make_database()

router = APIRouter()

@router.get("/api/install")
async def make_install():
    database_status = DatabaseConnector().hash_database()
    logger.debug(ORM_BASE.num_dashboardUsers())

    if database_status: 
        return {"message": "A software installation already exists"}
    
    try:
        DatabaseConnector().make_database()
        return DatabaseConnector().hash_database()
    except Exception as e:
        print(f"Error: {e}")
