from mcrcon import MCRcon
from loguru import logger

def test_rcon(command):
    with MCRcon("192.168.1.32", "custompassword", port=25575) as mcr:
        resp = mcr.command(command)
        logger.success(f"Command send: {command}")
        logger.success(f"Command response: {resp}")
        return resp
