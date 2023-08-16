from src.blocks import HTML


class HTMLBuilder:

    def __init__(self, formatter):
        self.formatter = formatter

    def build_html(self, yaml):
        content = (
            self._build_info_section(yaml)
            + self._build_settings_section(yaml)
            + self._build_params_section(yaml)
            + self._build_templates_section(yaml)
            + self._build_alarms_section(yaml)
            + self._build_report_section(yaml)
            + self._build_rules_section(yaml)
            + self._build_links_section(yaml)
            + self._build_locale_section(yaml)
        )
        html = HTML.page(content)
        return self.formatter.format_html(html)

    def _build_info_section(self, yaml):
        enabled = ['Deshabilitado', 'Habilitado']
        keys = [
            'publishBlockchain',
            'publishCertificates',
            'publishPrivateCertificate'
        ]
        values = [
            'Publicación en blockchain:',
            'Publicación justificantes:',
            'Publicación justificantes privados:'
        ]
        groups = [
            (value, enabled[int(yaml.get(key))], '')
            for key, value in zip(keys, values)
        ]
        rows = self._build_table_rows(groups, pg=True)
        return HTML.info_container(
            name=yaml.get('name'),
            description=yaml.get('description'),
            rows=''.join(rows)
        )

    def _build_settings_section(self, yaml):
        return self._build_dict_items(
            title='Ajustes',
            node=yaml.get('customSettings'),
            classes='blue'
        )

    def _build_params_section(self, yaml):
        return self._build_list_items(
            title='Parámetros',
            node=yaml.get('parameters'),
            classes='brown'
        )

    def _build_templates_section(self, yaml):
        return self._build_list_items(
            title='Plantillas',
            node=yaml.get('templates'),
            classes='green'
        )

    def _build_alarms_section(self, yaml):
        return self._build_list_items(
            title='Alarmas',
            node=yaml.get('alarmsDefinition'),
            classes='blue'
        )

    def _build_report_section(self, yaml):
        return self._build_list_dict_items(
            title = 'Informes',
            node = yaml.get('reportDefinition'),
            classes = 'brown'
        )

    def _build_rules_section(self, yaml):
        return self._build_list_dict_items(
            title = 'Reglas',
            node = yaml.get('rulesDefinition'),
            classes = 'green'
        )

    def _build_links_section(self, yaml):
        return self._build_dict_list_items(
            title = 'Enlaces',
            node = yaml.get('linksDefinition'),
            classes = 'blue'
        )

    def _build_locale_section(self, yaml):
        return self._build_dict_dict_items(
            title='Internacionalización',
            node=yaml.get('configLocale'),
            classes='brown bold'
        )

    def _build_list_items(self, title, node, classes):
        if not node:
            return ''

        headers = self._build_headers(node[0].keys())
        groups = [item.values() for item in node]
        rows = self._build_table_rows(groups)
        section = self._build_section(headers, rows, classes)
        return self._build_container(title, section)

    def _build_dict_items(self, node, title, classes):
        if not node:
            return ''

        values = ['name', 'value', 'description']
        headers = self._build_headers(values)
        groups = [(key, value, '') for key, value in node.items()]
        rows = self._build_table_rows(groups, pg=True)
        section = self._build_section(headers, rows, classes)
        return self._build_container(title, section)

    def _build_dict_dict_items(self, node, title, classes):
        if not node:
            return ''

        sections = [
            self._build_dict_items(value, key, classes)
            for key, value in node.items()
        ]
        section = ''.join(sections)
        return self._build_container(title, section, 'grupal')

    def _build_dict_list_items(self, title, node, classes):
        if not node:
            return ''

        header_group = [
            self._build_headers([key, 'grantedFields'])
            for key in node.keys()
        ]
        row_group = [
            [
                self._build_table_rows(
                    [(name, self._build_list(fields))]
                )
                for dic in lst
                for name, fields in [list(dic.values())]
            ]
            for lst in node.values()
        ]
        sections = [
            self._build_section(headers, rows, classes)
            for headers, rows in zip(header_group, row_group)
        ]
        return self._build_container(title, ''.join(sections))

    def _build_list_dict_items(self, title, node, classes):
        if not node:
            return ''

        headers = self._build_headers(node[0].keys())
        cell_groups = [
            [
                HTML.table_cell(self._build_table(value.items()))
                if isinstance(value, dict) else
                HTML.table_cell(value)
                for value in item.values()
            ]
            for item in node
        ]
        rows = [
            HTML.table_row(''.join(cells))
            for cells in cell_groups
        ]
        section = self._build_section(headers, ''.join(rows), classes)
        return self._build_container(title, section)

    def _build_headers(self, values):
        return [HTML.table_header(value) for value in values]

    def _build_table(self, cell_groups, pg=False):
        rows = self._build_table_rows(cell_groups, pg)
        return HTML.table(''.join(rows))

    def _build_table_rows(self, cell_groups, pg=False):
        return ''.join(
            HTML.table_row(''.join(
                HTML.table_cell_pg(cell)
                if pg else
                HTML.table_cell(cell)
                for cell in cells
            ))
            for cells in cell_groups
        )

    def _build_list(self, items):
        items = [HTML.list_item(item) for item in items]
        return HTML.ulist(''.join(items))

    def _build_section(self, headers, rows, classes):
        return HTML.section(
            headers=''.join(headers),
            rows=''.join(rows),
            classes=classes
        )

    def _build_container(self, title, section, classes=None):
        return HTML.section_container(
            id=self.formatter.format_id(title),
            title=title,
            sections=section,
            classes=classes
        )
