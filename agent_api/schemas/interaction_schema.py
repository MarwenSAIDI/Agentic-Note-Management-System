from sqlmodel import SQLModel
from agent_api.schemas.role_enum_schema import RoleEnum

class Interaction(SQLModel, table=False):
    role: RoleEnum
    query: str