import sdRDM

from typing import List, Optional
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .nested import Nested


@forge_signature
class ModelObject(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("modelobjectINDEX"),
        xml="@id",
    )

    value: Optional[str] = Field(
        default=None,
        description="This is a primitive",
    )

    nested: Optional[Nested] = Field(
        default=Nested(),
        description="This is a nested object",
    )

    multiple_values: List[str] = Field(
        description="This is an array of primitives",
        default_factory=ListPlus,
        multiple=True,
    )

    multiple_nested: List[Nested] = Field(
        description="This is an array of nested objects",
        default_factory=ListPlus,
        multiple=True,
    )

    def add_to_multiple_nested(
        self, value: Optional[float] = None, id: Optional[str] = None
    ) -> None:
        """
        This method adds an object of type 'Nested' to attribute multiple_nested

        Args:
            id (str): Unique identifier of the 'Nested' object. Defaults to 'None'.
            value (): Value of the nested object. Defaults to None
        """

        params = {
            "value": value,
        }

        if id is not None:
            params["id"] = id

        self.multiple_nested.append(Nested(**params))

        return self.multiple_nested[-1]
