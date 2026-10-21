import json
from pathlib import Path

def transliterate(lang, string):
    path = Path('../assets/languages.json')
    content = path.read_text()
    dic = json.loads(content)[lang]

    keys = sorted(dic.keys(), key=len, reverse=True)

    result = []
    p = 0
    while p < len(string):
        matched = False
        for key in keys:
            if string[p:p+len(key)] == key:
                result.append(dic[key])
                p += len(key)
                matched = True
                break
        if not matched:
            result.append(string[p])
            p += 1

    return ''.join(result)


