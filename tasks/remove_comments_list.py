def remove_comments(source):
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
