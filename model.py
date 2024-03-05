from pydantic import BaseModel


class BuildRCRMapRequest(BaseModel):
    commands: list[str]


class BuildRCRMapResult(BaseModel):
    rcr_map: dict
