import rich

from Test.core import ModelObject, Nested

dataset = ModelObject(
    value="Hello World",
    multiple_values=["This", "is", "a", "list", "of", "strings"],
)

# Single nested case
nested = Nested(value=100.0)

# Multiple nested case
for i in range(5):
    dataset.add_to_multiple_nested(value=i)

# Define expectation
expected = {
    "id": "modelobject0",
    "value": "Hello World",
    "multiple_values": ["This", "is", "a", "list", "of", "strings"],
    "multiple_nested": [
        {"id": "nested2", "value": 0.0},
        {"id": "nested3", "value": 1.0},
        {"id": "nested4", "value": 2.0},
        {"id": "nested5", "value": 3.0},
        {"id": "nested6", "value": 4.0},
    ],
    "__source__": {"root": "ModelObject"},
}

to_test = dataset.to_dict(warn=False)
to_test.update({"__source__": {"root": "ModelObject"}})

assert to_test == expected, "❌ Generated API does not match expected output"


rich.print(dataset.to_dict(warn=False))
