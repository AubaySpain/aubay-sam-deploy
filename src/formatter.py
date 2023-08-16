import unicodedata

import cssbeautifier
import jsbeautifier
from bs4 import BeautifulSoup


class HTMLFormatter:

    def format_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        for tag in soup.find_all('style'):
            self._format_tag(tag, cssbeautifier)
        for tag in soup.find_all('script'):
            self._format_tag(tag, jsbeautifier)
        return soup.prettify()

    def _format_tag(self, tag, formatter):
        raw = tag.string
        opts = {'indent_size': 2, 'indent_level': 2}
        fmt = formatter.beautify(raw, opts)
        raw.replace_with(fmt)

    def format_id(self, title):
        return (
            unicodedata
            .normalize('NFKD', title)
            .encode('ascii', 'ignore')
            .decode('utf-8')
            .replace(' ', '-')
            .lower()
        )
