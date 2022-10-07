from pydantic import BaseModel, Field


class Expression(BaseModel):
    phrase: str = Field(description="Математическое выражение")

    class Config:
        schema_extra = {
            "example": {
                "phrase": "(5 + (( 4 * 2 ) * ( 2 + 3 )))",
            }
        }