def buy(list):
    print('\n[구입]')
    item = input('상품명? ')
    if item == '' :
        return False
    else :
        amount = int(input('수량은? '))
        list[item] = amount
        print(f'장바구니에 {item}가(이) {amount}개가 담겼습니다.')

def show(list):
    print(f'\n>>> 장바구니 보기: {list}')

def find(list) :
    print('\n[검색]')
    f_item = input('장바구니에서 확인하고자 하는 상품은? ')
    if f_item in list:
        print(f'{f_item}은(는) {list[f_item]}개 담겨 있습니다.')
    else :
        print(f'장바구니에 {f_item}은(는) 없습니다.')

shopping_bag = {}

while True:
    if buy(shopping_bag) == False :
        break
show(shopping_bag)
find(shopping_bag)