import rich

from Test.core import ModelObject, Nested

dataset = ModelObject(
    value="Hello World",
    multiple_values=["This", "is", "a", "list", "of", "strings"],
)
