def remove_comments_v0(source):
    block = False
    res = []
    for line in source:
        if block == False:
            line_out = ''
        pos = 0
        while pos < len(line) and not (block == False and line[pos:pos + 2] == '//'):
            switch = line[pos:pos + 2]
            if block and switch == '*/' or block == False and switch == '/*':
                block = not block
                pos += 2
            else:
                if block == False:
                    line_out += line[pos]
                pos += 1
        if line_out != '' and block == False:
            res.append(line_out)
    return res

def remove_comments(lines):
    s = '\n'.join(lines)
    pos = 0
    out = []
    while pos < len(s):
        if s[pos: pos+2] not in ['//', '/*']:
            out.append(s[pos])
            pos += 1
            continue
        pos += 2
        if s[pos-1] == '/':
            while pos < len(s) and s[pos] != '\n':
                pos += 1
            continue
        while pos < len(s) and s[pos: pos+2] != '*/':
            pos += 1
        pos += 2
    return [line for line in ''.join(out).split('\n') if line]
