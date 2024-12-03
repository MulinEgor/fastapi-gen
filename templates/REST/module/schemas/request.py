from pydantic import BaseModel


class {capitalized_name}CreateSchema(BaseModel):
    pass


class {capitalized_name}UpdateSchema({capitalized_name}CreateSchema):
    """
    Update schema, contains all fields from the create schema,
    but all fields can be optional
    """ 
    class Config:
        from_attributes = True

    def __init__(self, **data):
        super().__init__(**data)
        for field in self.model_fields.values():
            field.required = False

