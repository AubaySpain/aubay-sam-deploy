from src.builder import HTMLBuilder
from src.formatter import HTMLFormatter
from src.processor import FileProcessor


def main():
    formatter = HTMLFormatter()
    builder = HTMLBuilder(formatter)
    processor = FileProcessor(builder)
    processor.start()


if __name__ == '__main__':
    main()
