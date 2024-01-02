from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class CamelCaseBaseModel(BaseModel):
    """Camel case model for input & output schemas."""

    def to_json(self):
        """Convert the model to JSON with CamelCase."""
        return self.model_dump_json(by_alias=True)

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)


__all__ = ["CamelCaseBaseModel"]
