# aubay-sam-deploy
Deploy &amp; Documentation tool for Aubay SAM specifications

## SAM_DOC_GEN
> Sam Documentation Generator

This module allows the conversion of a file in YAML format to an HTML file.

The generated HTML document presents the OpenAPI style, by default, describing each YAML grouping as an OpenAPI endpoint grouping (sections).

The connectors approach assumes the existence of the 'specifications' directory, where each of the specifications will be distributed.


Script Example:

`python sam_doc_gen/yaml_to_html.py --in connector --source isylight/calle --out folder`

Compile project:

```bash
python3 -m build
```

Test compilation:

```bash
python3 -m venv .env/fresh-install-test
. .env/fresh-install-test/bin/activate
pip install dist/aubay_sam_deploy-<<version>>-py3-none-any.whl

# Can use `generate-active` command
generate-active --source isylight/calle

# Or `generate-active-report` command
generate-active-report --in file --source sample.yaml --out folder

# to uninstall and quit
pip uninstall aubay-sam-deploy
deactive
```

Test by TestPypi:

```bash
python3 -m twine upload --verbose --config-file .devcontainer/.pypirc --repository testpypi dist/*
```
