def remove_marks(text: str, marks: str) -> str:
    remove_marks.__dict__.setdefault('count', 0)
    for sym in marks:
        text = text.replace(sym, '')
    remove_marks.count += 1
    return text

# еще вариант
# def remove_marks(text,marks):
#     remove_marks.count +=1
#     return ''.join(c for c in text if c not in marks)
#
# remove_marks.count = 0

