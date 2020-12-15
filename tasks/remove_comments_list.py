def remove_comments(source):
    default = 0
    single_comment = 1
    multi_comment = 2
    mode = default
    res = []
    for line in source:
        if mode == single_comment:
            mode = default
        line_out = ''
        max_pos = len(line) - 1
        pos = 0
        while pos <= max_pos:
            sym = line[pos]
            if mode == default:
                if sym == '/' and pos < max_pos and \
                        line[pos + 1] in ['/', '*']:
                    sym += line[pos + 1]
                    pos += 1
                if sym == '//':
                    mode = single_comment
                elif sym == '/*':
                    mode = multi_comment
                else:
                    line_out += sym
            elif mode == multi_comment:
                if pos < max_pos and line[pos:pos + 2] == '*/':
                    mode = default
                    pos += 1
            pos += 1
        if line_out != '':
            res.append(line_out)
    return res
