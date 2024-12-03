from api.{name}.repository import {capitalized_name}Repository
from api.{name}.service import {capitalized_name}Service


def get_{name}_service():
    return {capitalized_name}Service({capitalized_name}Repository())
