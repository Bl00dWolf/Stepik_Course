def non_closed_files(files: list) -> list:
    opened = []
    for file in files:
        if not file.closed:
            opened.append(file)
    return opened

# еще вариант
# def non_closed_files(files):
#     return [file for file in files if not file.closed]