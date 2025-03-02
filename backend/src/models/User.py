from pydantic import BaseModel


class IncomingUser(BaseModel):
    name: str
    password: str