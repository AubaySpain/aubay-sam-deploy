# import os
# import tempfile
# from argparse import Namespace

# import pytest

# from src.builder import HTMLBuilder
# from src.formatter import HTMLFormatter
# from src.logger import Exit
# from src.processor import FileProcessor


# class TestFileProcessor:

#     def setup_method(self):
#         formatter = HTMLFormatter()
#         self.builder = HTMLBuilder(formatter)
#         self.processor = FileProcessor(self.builder)

#     def test_parse_args(self):
#         with pytest.raises(SystemExit):
#             self.processor._parse_args(['--source', 'source.yaml'])

#         with pytest.raises(SystemExit):
#             self.processor._parse_args(['--target', 'target.html'])

#         with pytest.raises(SystemExit):
#             self.processor._parse_args([])

#         args = self.processor._parse_args(['--source', 'source.yaml', '--target', 'target.html'])
#         assert args.source == 'source.yaml'
#         assert args.target == 'target.html'

#     def test_check_paths(self):
#         with tempfile.NamedTemporaryFile(delete=False) as source_file:
#             source_file_path = source_file.name

#         with tempfile.NamedTemporaryFile(delete=False) as target_file:
#             target_file_path = target_file.name

#         source = os.path.abspath(source_file_path)
#         target = os.path.abspath(target_file_path)

#         self.processor._check_paths(source, target)

#         os.unlink(source_file_path)
#         os.unlink(target_file_path)

#         with pytest.raises(Exit):
#             self.processor._check_paths('invalid_source.yaml', 'invalid_target.html')

#         with pytest.raises(Exit):
#             self.processor._check_paths(source, 'invalid_folder/invalid_target.html')

#     def test_check_structure(self):
#         yaml = {'name': 'John', 'age': 30}
#         self.processor._check_structure(yaml)

#         yaml = {'name': 'John', 'age': 'thirty'}
#         with pytest.raises(ValueError):
#             self.processor._check_structure(yaml)

#         yaml = {'name': 'John', 'age': 30, 'address': {'city': 'New York', 'state': 'NY'}}
#         with pytest.raises(ValueError):
#             self.processor._check_structure(yaml)

#     def test_generate_report(self):
#         with tempfile.NamedTemporaryFile(mode='w', delete=False) as source_file:
#             source_file.write('name: John\nage: 30\n')
#             source_file_path = source_file.name

#         with tempfile.NamedTemporaryFile(mode='w', delete=False) as target_file:
#             target_file_path = target_file.name

#         self.processor._parse_args = lambda: Namespace(
#             source=source_file_path,
#             target=target_file_path
#         )

#         self.processor._generate_report(source_file_path, target_file_path)

#         with open(target_file_path, 'r') as f:
#             result = f.read()

#         expected = (
#             '<table>\n'
#             '<tr><th>name</th><td>John</td></tr>\n'
#             '<tr><th>age</th><td>30</td></tr>\n'
#             '</table>'
#         )

#         assert result.strip() == expected.strip()

#         os.unlink(source_file_path)
#         os.unlink(target_file_path)

#         with pytest.raises(Exit):
#             self.processor._generate_report('invalid_source.yaml', 'invalid_target.html')

#         with pytest.raises(Exit):
#             self.processor._generate_report(source_file_path, 'invalid_folder/invalid_target.html')

#         with pytest.raises(ValueError):
#             self.processor._generate_report(
#                 source_file_path, f'{target_file_path}.invalid'
#             )

#         with pytest.raises(Exception):
#             self.processor._generate_report(
#                 f'{source_file_path}.invalid', target_file_path
#             )

#     def test_start(self):
#         with tempfile.NamedTemporaryFile(mode='w', delete=False) as source_file:
#             source_file.write('name: John\nage: 30\n')
#             source_file_path = source_file.name

#         with tempfile.NamedTemporaryFile(mode='w', delete=False) as target_file:
#             target_file_path = target_file.name

#         self.processor._parse_args = lambda: Namespace(
#             source=source_file_path,
#             target=target_file_path
#         )

#         self.processor.start()

#         with open(target_file_path, 'r') as f:
#             result = f.read()

#         expected = (
#             '<table>\n'
#             '<tr><th>name</th><td>John</td></tr>\n'
#             '<tr><th>age</th><td>30</td></tr>\n'
#             '</table>'
#         )

#         assert result.strip() == expected.strip()

#         os.unlink(source_file_path)
#         os.unlink(target_file_path)

#         with pytest.raises(Exit):
#             self.processor.start('invalid_source.yaml', 'invalid_target.html')

#         with pytest.raises(Exit):
#             self.processor.start(source_file_path, 'invalid_folder/invalid_target.html')

#         with pytest.raises(ValueError):
#             self.processor.start(source_file_path, f'{target_file_path}.invalid')

#         with pytest.raises(Exception):
#             self.processor.start(f'{source_file_path}.invalid', target_file_path)
