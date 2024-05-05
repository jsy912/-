shopping_bag = []
n_shopping_bag = {}

print('[구입]')
while True:
    item = input('상품명? ')
    if item == '' :
        break
    shopping_bag.append(item)
    n_item = int(input('수량은? '))
    n_shopping_bag[item] = n_item
    print(f'장바구니에 {item} {n_item}개가 담겼습니다.\n')
    
print(f'\n>>> 장바구니 보기: {n_shopping_bag}')

print('\n[검색]')
searching_item = input('장바구니에서 확인하고자 하는 상품은? ')
if searching_item in n_shopping_bag :
    print(f'{searching_item}은(는) {n_shopping_bag[searching_item]}개 담겨 있습니다.')
else :
    print('해당 상품은 존재하지 않습니다.')