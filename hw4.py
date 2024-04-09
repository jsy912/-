def rep_char(c, n) :
    print(c * n)

def draw_line_string(name) :
    msg1 = (f'Hello {name},')
    msg2 = ('Welcome to Seoul.')
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    rep_char('-', nstr + 2)
    print(f' {msg1} ')
    print(f' {msg2} ')
    rep_char('-', nstr + 2)

name1 = input('Input his/her name: ')
draw_line_string(name1)
name2 = input('Input his/her name: ')
draw_line_string(name2)