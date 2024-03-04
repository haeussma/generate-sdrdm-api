# Software-driven RDM Python API Generator Action

![Tests](https://github.com/JR-1991/generate-sdrdm-api/actions/workflows/test_action.yml/badge.svg)

This is a GitHub Action that generates Python API's from sdRDM markdown schemes and pushes them to the repository.

> **Note:** If you want changes to be pushed to your repository, you need to grant action read and write access. This can be done in the `settings/actions` tab of your repository.

<p align="center" >
  <img
    src="https://i0.wp.com/user-images.githubusercontent.com/185122/115415646-1487b780-a1c5-11eb-99e2-1cafe81873b5.png?ssl=1"
    width="600"
  />
</p>

## Usage

```yaml
# Generates API and pushes it to the root of the repository
- name: Generate sdRDM library
  uses: JR-1991/generate-sdrdm-api@main
  with:
    library_name: "MyLibraryName"
    schema_path: "./path/to/schema"

# Generates API and pushes it to the specified directory
- name: Generate sdRDM library
  uses: JR-1991/generate-sdrdm-api@main
  with:
    library_name: "MyLibraryName"
    schema_path: "./path/to/schema"
    out_dir: "./other/dir"

# Generates API and does not push it to the repository
- name: Generate sdRDM library
  uses: JR-1991/generate-sdrdm-api@main
  with:
    library_name: "MyLibraryName"
    schema_path: "./path/to/schema"
    push: "false"
```

## Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

|                                   INPUT                                    |  TYPE  | REQUIRED |        DEFAULT        |                                                                  DESCRIPTION                                                                  |
|----------------------------------------------------------------------------|--------|----------|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
|             <a name="input_branch"></a>[branch](#input_branch)             | string |  false   |                       | The sdRDM branch to be <br>used for the generated API. <br>Meant for dev purposes. Standard <br>installaton uses the latest pip <br>release.  |
|    <a name="input_library_name"></a>[library_name](#input_library_name)    | string |   true   |                       |                                                 The name of the library <br>to be generated.                                                  |
|           <a name="input_out_dir"></a>[out_dir](#input_out_dir)            | string |   true   |        `"./"`         |                                                 Target directory for the generated <br>API.                                                   |
|                <a name="input_push"></a>[push](#input_push)                | string |   true   |       `"true"`        |                                             Push the generated API to <br>the specified branch.                                               |
|             <a name="input_schema"></a>[schema](#input_schema)             | string |   true   |       `"false"`       |                                                          Generate the sdRDM schema.                                                           |
| <a name="input_schema_out_dir"></a>[schema_out_dir](#input_schema_out_dir) | string |   true   |        `"./"`         |                                                Target directory for the generated <br>schema.                                                 |
|     <a name="input_schema_path"></a>[schema_path](#input_schema_path)      | string |   true   | `"./specifications/"` |                                                           Path to the sdRDM schema.                                                           |

<!-- AUTO-DOC-INPUT:END -->
