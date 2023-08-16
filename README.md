# SAM Documentation generator

This is a simple documentation generator for SAM templates.
It will generate a HTML file from a YAML file.

## Usage
python main.py --source __SOURCE_PATH__ --target __TARGET_PATH__

## Example
python main.py --source ./specifications/specification.yaml --target ./specifications/specification.html

## Tests
pytest -v
