import re

import pytest

from src.formatter import HTMLFormatter


class TestFormatter:

    def setup_method(self):
        self.formatter = HTMLFormatter()

    def test_format_html(self):
        html = (
            '<html>'
            '<head>'
            '<style>body{color:red;}</style>'
            '</head>'
            '<body>'
            '<h1>Test</h1>'
            '<script>alert("Test");</script>'
            '</body>'
            '</html>'
        )
        result = self.formatter.format_html(html)
        assert result != html
        assert re.sub(r'\s+', '', result) == html

    def test_format_id(self):
        title = 'This is a Test áéíóúñ'
        expected = 'this-is-a-test-aeioun'
        result = self.formatter.format_id(title)
        assert result == expected


if __name__ == '__main__':
    pytest.main()
