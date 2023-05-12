def sourcetemplate(url: str):
    def reargs(**kwargs):
        nonlocal url
        url += '?'
        for name, val in sorted(kwargs.items()):
            url += f'{name}={val}&'
        return url[:-1]
    return reargs

url = 'https://all_for_comfort_life.com'
load = sourcetemplate(url)
print(load(smartphone='iPhone', notebook='huawei', sale=True))
