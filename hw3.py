def get_fixed_price(discount_rate, discounted_priced) :
    original_price = int(discounted_priced / (1 - (discount_rate / 100)))
    return original_price

rate = int(input('할인율은? '))
discounted_price_A = int(input('A 상품의 할인된 가격은? '))
discounted_price_B = int(input('B 상품의 할인된 가격은? '))
original_price_A = get_fixed_price(rate, discounted_price_A)
original_price_B = get_fixed_price(rate, discounted_price_B)
print('A 상품의 정가는', original_price_A, '원')
print('B 상품의 정가는', original_price_B, '원')