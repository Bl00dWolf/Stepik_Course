import string as st


def convert(string):
    mapping = list(map(lambda c: 1 if c in st.ascii_lowercase else 2 if c in st.ascii_uppercase else 0, string))
    if mapping.count(1) >= mapping.count(2):
        return string.lower()
    else:
        return string.upper()