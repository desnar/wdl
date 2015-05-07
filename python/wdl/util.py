def md_table(table, header):
    max_len = 64
    col_size = [len(x) for x in header]
    def trunc(s):
        return s[:max_len-3] + '...' if len(s) >= max_len else s
    for row in table:
        for index, cell in enumerate(row):
            if len(str(cell)) > col_size[index]:
                col_size[index] = min(len(str(cell)), max_len)
    def make_row(row):
        return '|{}|'.format('|'.join([trunc(str(x)).ljust(col_size[i]) if x is not None else ' ' * col_size[i] for i,x in enumerate(row)]))
    r = make_row(header) + '\n'
    r += '|{}|'.format('|'.join(['-' * col_size[i] for i,x in enumerate(col_size)])) + '\n'
    r += '\n'.join([make_row(x) for x in table])
    return r
