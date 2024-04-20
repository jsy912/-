def display_multiplication_table(s, e):
    i = 1
    while i <= 9 :
        for n in range(s, e):
            print(f'{n} x {i} = {n * i:2d}', end='     ')
        i += 1
        print()

display_multiplication_table(2, 6)
print()
display_multiplication_table(6, 10)