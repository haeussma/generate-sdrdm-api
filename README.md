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
