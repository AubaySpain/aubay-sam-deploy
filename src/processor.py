from argparse import ArgumentParser
from pathlib import Path

import oyaml

from src.logger import Exit
from src.models import YAMLModel


class FileProcessor:

    def __init__(self, builder):
        self._builder = builder

    def start(self):
        args = self._parse_args()
        source = Path(args.source)
        target = Path(args.target)
        self._check_paths(source, target)
        self._generate_report(source, target)

    def _parse_args(self):
        parser = ArgumentParser(
            description='YAML to HTML file converter'
        )
        parser.add_argument(
            '--source',
            help='Input file from which to read the data',
            required=True
        )
        parser.add_argument(
            '--target',
            help='Output file to which to write the data',
            required=True
        )
        return parser.parse_args()

    def _check_paths(self, source, target):
        if not source.is_file():
            Exit.warning(f"Input file '{source}' does not exist")

        if not (parent := target.parent).is_dir():
            Exit.warning(f"Output folder '{parent}' does not exist")

    def _generate_report(self, source, target):
        try:
            text = source.read_text('utf-8')
            yaml = oyaml.load(text, oyaml.SafeLoader)
            self._check_structure(yaml)
            html = self._builder.build_html(yaml)
            target.write_text(html, 'utf-8')
            Exit.success(f"File '{target}' has been generated")

        except ValueError as err:
            Exit.error(f"File '{source}' validation error:", err)

        except Exception as ex:
            Exit.error(f"File '{target}' exception:", ex)

    def _check_structure(self, yaml):
        YAMLModel(**yaml)
