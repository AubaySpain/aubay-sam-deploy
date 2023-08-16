from unittest.mock import patch

import pytest

from src.logger import CLEAR, GREEN, RED, RESET, YELLOW, Exit


class TestLogger:

    @patch('src.logger.sys.exit')
    @patch('builtins.print')
    def test_success(self, mock_print, mock_exit):
        Exit.success('Test')
        expected = f'{CLEAR}{GREEN}SUCCESS: {RESET}Test\n'
        mock_print.assert_called_once_with(expected)
        mock_exit.assert_called_once_with(0)

    @patch('src.logger.sys.exit')
    @patch('builtins.print')
    def test_warning(self, mock_print, mock_exit):
        Exit.warning('Test')
        expected = f'{CLEAR}{YELLOW}WARNING: {RESET}Test\n'
        mock_print.assert_called_once_with(expected)
        mock_exit.assert_called_once_with(1)

    @patch('builtins.print')
    def test_error(self, mock_print):
        with pytest.raises(Exception):
            Exit.error('Test', Exception('Test'))
        expected = f'{CLEAR}{RED}ERROR: {RESET}Test\n'
        mock_print.assert_called_once_with(expected)


if __name__ == '__main__':
    pytest.main()
