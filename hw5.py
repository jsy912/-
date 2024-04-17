def read_single_digit(digit):
    if digit == 0 :
        return '영'
    elif digit == 1 :
        return '일'
    elif digit == 2 :
        return '이'
    elif digit == 3 :
        return '삼'
    elif digit == 4 :
        return '사'
    elif digit == 5 :
        return '오'
    elif digit == 6 :
        return '육'
    elif digit == 7 :
        return '칠'
    elif digit == 8 :
        return '팔'
    else :
        return '구'

def read_number(number):
    h_digit = number // 100
    number %= 100
    t_digit = number // 10
    number %= 10
    s_digit = number
    return f'{read_single_digit(h_digit)} {read_single_digit(t_digit)} {read_single_digit(s_digit)}'

number = int(input('세 자리 정수 입력: '))
print(read_number(number))