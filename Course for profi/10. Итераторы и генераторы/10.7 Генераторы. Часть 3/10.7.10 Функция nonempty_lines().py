def nonempty_lines(file: str):
    with open(file, encoding='utf-8') as fl:
        yield from (line.strip() if len(line.strip()) > 25 else '...' for line in fl if line.strip())
