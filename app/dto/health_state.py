from pydantic import BaseModel


class HealthState(BaseModel):
    state: str
