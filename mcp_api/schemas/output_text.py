from pydantic import BaseModel
from schemas.output_type_enum import OutputTypeEnum

class OutputText(BaseModel):
    type: OutputTypeEnum
    source: str = ""
    title: str
    content: str