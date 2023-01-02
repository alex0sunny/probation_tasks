'''
Смайликом считается последовательность, начинающаяся с символа : или ; , далее могут следовать символы -
и заканчивается скобками ()[]{}. Никакие другие символы не могут участвовать в смайлике.
Задача: удалить смайлики из строки.
'''


def remove_smiles(s):
    pos = 0
    out = []
    while pos < len(s):
        if s[pos] not in ';:':
            out.append(s[pos])
            pos += 1
            continue
        back = pos
        pos += 1
        while pos < len(s) and s[pos] == '-':
            pos += 1
        while pos < len(s) and s[pos] in '(){}[]':
            pos += 1
        if s[pos-1] not in '(){}[]':
            out.extend(s[back:pos])
    return ''.join(out)


assert remove_smiles(';--)') == ''
assert remove_smiles(';) abc::-----()()() a') == ' abc: a'
assert remove_smiles('') == ''
