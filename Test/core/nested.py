import sdRDM

from typing import Optional
from pydantic import Field
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Nested(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("nestedINDEX"),
        xml="@id",
    )

    value: Optional[float] = Field(
        default=None,
        description="Value of the nested object",
    )
