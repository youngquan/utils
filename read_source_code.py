from pathlib import Path
import re

comment_pattern = re.compile(r'#.*\n')
docstring_pattern = re.compile(r'""".*?"""\n', re.S)

root_path = '.'
with open('result.txt', 'w', encoding='utf8') as out:
    for file in Path(root_path).glob('**/*.py'):
        if str(file) == 'read_source_code.py':
            continue
        out.write(f'# {file} \n')
        with file.open(encoding='utf-8') as f:
            content = f.read()
        content_no_comment = comment_pattern.sub('', content)
        content_no_docstring = docstring_pattern.sub('', content_no_comment)
        out.write(content_no_docstring)
        out.write('\n')
