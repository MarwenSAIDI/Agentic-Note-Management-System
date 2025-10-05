from sqlmodel import SQLModel, Field
from typing import Optional

class ChatSession(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, index=True)
    private_key: str
    public_key: str