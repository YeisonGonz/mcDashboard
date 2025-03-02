from mcrcon import MCRcon
from loguru import logger
from dotenv import load_dotenv
import os
load_dotenv()

HOST = os.getenv('MINECRAFT_RCON_HOST')
PASSWORD = os.getenv('MINECRAFT_RCON_PASSWORD')
PORT = int(os.getenv('MINECRAFT_RCON_PORT'))

def test_rcon(command):
    with MCRcon(HOST, PASSWORD, port=PORT) as mcr:
        resp = mcr.command(command)
        logger.success(f"Command send: {command}")
        logger.success(f"Command response: {resp}")
        return resp
