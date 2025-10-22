from pydantic import BaseModel, ConfigDict


class BaseSchemaForDB(BaseModel):
    id: int

    model_config = ConfigDict(from_attributes=True)
