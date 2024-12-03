from pydantic import BaseModel


class {capitalized_name}ModuleConfig(BaseModel):
    prefix: str = "/{name}"
    tags: list[str] = ["{capitalized_name}"]
