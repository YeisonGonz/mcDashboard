from fastapi import APIRouter, Depends, HTTPException
from loguru import logger
from src.auth.jwtAuth import get_current_user
from src.models.GeneralModels import MinecraftCommand
from src.rcon.rconClient import test_rcon

router = APIRouter()    

@router.post("/api/command")
async def rcon_send_command(command: MinecraftCommand, current_user: bool = Depends(get_current_user)):
    try:
        response = test_rcon(command.command)
        return {"message": response}
    except Exception:
        return HTTPException(status_code=500, detail="Failed to send command to server.")