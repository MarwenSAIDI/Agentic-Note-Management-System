from sqlmodel import SQLModel, Field
from typing import Optional
from agent_api.schemas.role_enum_schema import RoleEnum

class Interaction(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, index=True)
    session_id: Optional[int] = Field(foreign_key='session.id')
    role: RoleEnum
    query: str