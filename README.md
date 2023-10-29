# Generate Python API's from sdRDM markdown schema

This is a GitHub Action that generates Python API's from sdRDM markdown schemes and pushes them to the repository.

> **Note:** If you want changes to be pushed to your repository, you need to grant action read and write access. This can be done in the `settings/actions` tab of your repository.

## Usage

```yaml
# Generates API and pushes it to the root of the repository
- name: Generate sdRDM library
  uses: ./
  with:
    library_name: "MyLibraryName"
    schema_path: "./path/to/schema"

# Generates API and pushes it to the specified directory
- name: Generate sdRDM library
  uses: ./
  with:
    library_name: "MyLibraryName"
    schema_path: "./path/to/schema"
    output_path: "./other/dir"

# Generates API and does not push it to the repository
- name: Generate sdRDM library
  uses: ./
  with:
    library_name: "MyLibraryName"
    schema_path: "./path/to/schema"
    push: "false"
```

## Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|                                INPUT                                 |  TYPE  | REQUIRED |       DEFAULT        |                       DESCRIPTION                       |
|----------------------------------------------------------------------|--------|----------|----------------------|---------------------------------------------------------|
|          <a name="input_branch"></a>[branch](#input_branch)          | string |   true   | `"linking-refactor"` | The sdRDM branch to be <br>used for the generated API.  |
| <a name="input_library_name"></a>[library_name](#input_library_name) | string |   true   |     `"unstable"`     |      The name of the library <br>to be generated.       |
|        <a name="input_out_dir"></a>[out_dir](#input_out_dir)         | string |   true   |        `"./"`        |      Target directory for the generated <br>API.        |
|             <a name="input_push"></a>[push](#input_push)             | string |   true   |       `"true"`       |  Push the generated API to <br>the specified branch.    |
|  <a name="input_schema_path"></a>[schema_path](#input_schema_path)   | string |   true   | `"./specifcations/"` |                Path to the sdRDM schema.                |

<!-- AUTO-DOC-INPUT:END -->
