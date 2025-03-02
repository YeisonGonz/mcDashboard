from fastapi import FastAPI
from loguru import logger
from src.routers.databaseRouter import router as DatabaseRouter
from src.routers.installRouter import router as InstallRouter
from src.routers.rconRouter import router as MCRconRouter

logger.add("src/logs/log_file.log", rotation=10000, retention=1)

app = FastAPI()

app.include_router(DatabaseRouter)
app.include_router(MCRconRouter)
app.include_router(InstallRouter)



@app.get("/")
async def root():
    return {"message": "Hello World"}