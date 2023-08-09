from argparse import ArgumentParser
from pathlib import Path

import cssbeautifier
import oyaml
from bs4 import BeautifulSoup
from cssbeautifier.css.options import BeautifierOptions

from blocks import HTMLBlocks
from logger import Exit


class FileProcessor:

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
            html = self._build_html(yaml)
            target.write_text(html, 'utf-8')
            Exit.success(f"File '{target}' has been generated")

        except Exception as ex:
            Exit.error(f"File '{target}' exception: {ex}")

    def _build_html(self, yaml):
        content = (
            self._build_info_section(yaml)
            + self._build_settings_section(yaml)
            + self._build_params_section(yaml)
            + self._build_templates_section(yaml)
            + self._build_locale_section(yaml)
            + self._build_alarms_section(yaml)
            + self._build_report_section(yaml)
        )
        html = HTMLBlocks.page.substitute(content=content)
        return self._format_html(html)

    def _build_info_section(self, yaml):
        is_enabled = lambda x: 'Habilitado' if x else 'Deshabilitado'

        keys = [
            'Publicación en blockchain:',
            'Publicación justificantes:',
            'Publicación justificantes privados:'
        ]
        values = [
            'publishBlockchain',
            'publishCertificates',
            'publishPrivateCertificate'
        ]
        items = [
            HTMLBlocks.items.substitute(
                key=key,
                value=is_enabled(yaml.get(value)),
                title=''
            )
            for key, value in zip(keys, values)
        ]
        return HTMLBlocks.info.substitute(
            name=yaml.get('name'),
            description=yaml.get('description'),
            items=''.join(items)
        )

    def _build_settings_section(self, yaml):
        return self._build_dict_items(
            node=yaml.get('customSettings'),
            title='Ajustes',
            classes='get'
        )

    def _build_params_section(self, yaml):
        return self._build_list_items(
            node=yaml.get('parameters'),
            title='Parámetros',
            classes='good'
        )

    def _build_templates_section(self, yaml):
        return self._build_list_items(
            node=yaml.get('templates'),
            title='Plantillas',
            classes='good'
        )

    def _build_locale_section(self, yaml):
        return self._build_dict_dict_items(
            node=yaml.get('configLocale'),
            title='Internacionalización',
            classes='put'
        )

    def _build_alarms_section(self, yaml):
        return self._build_list_items(
            node=yaml.get('alarmsDefinition'),
            title='Alarmas',
            classes='good'
        )

    def _build_report_section(self, yaml):
        return self._build_list_items(
            node=yaml.get('reportDefinition'),
            title='Informes',
            classes='get'
        )

    def _build_list_items(self, node, title, classes):
        if not isinstance(node, list):
            return ''

        keys = node[0].keys()
        labels = [
            HTMLBlocks.props_label.substitute(label=key)
            for key in keys
        ]
        items = [
            f'''
                <tr>
                {''.join(
                    HTMLBlocks.props_value
                    .substitute(value=item.get(key))
                    for key in keys
                )}
                </tr>
            '''
            for item in node
        ]
        return self._build_container(title, labels, items, classes)

    def _build_dict_items(self, node, title, classes):
        if not isinstance(node, dict):
            return ''

        labels = [
            HTMLBlocks.props_label.substitute(label='name'),
            HTMLBlocks.props_label.substitute(label='value'),
            HTMLBlocks.props_label.substitute(label='description')
        ]
        items = [
            HTMLBlocks.items.substitute(
                key=item,
                value=node.get(item),
                title=''
            )
            for item in node
        ]
        return self._build_container(title, labels, items, classes)

    def _build_dict_dict_items(self, node, title, classes):
        if not isinstance(node, dict):
            return ''

        items = ''.join(
            self._build_dict_items(node.get(key), key, classes)
            for key in node
        )
        return HTMLBlocks.props.substitute(
            title=title,
            items=items,
            classes='grupal operations'
        )

    def _build_container(self, title, labels, items, classes):
        items = HTMLBlocks.props_item.substitute(
            classes=f'{classes} operation',
            labels=''.join(labels),
            items=''.join(items)
        )
        return HTMLBlocks.props.substitute(
            title=title,
            items=items,
            classes='operations'
        )

    def _format_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        tag = soup.find('style').string
        opts = BeautifierOptions({
            'indent_size': 2,
            'indent_level': 2
        })
        css = cssbeautifier.beautify(tag, opts)
        tag.replace_with(css)
        return soup.prettify()


if __name__ == '__main__':
    processor = FileProcessor()
    processor.start()
