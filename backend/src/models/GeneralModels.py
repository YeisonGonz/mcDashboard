from pydantic import BaseModel


class MinecraftCommand(BaseModel):
    command: str