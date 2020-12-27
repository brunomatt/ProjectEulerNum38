# Take the number 192 and multiply it by each of 1, 2, and 3:
#
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

pandigital_products = []

def deconstruct(num): #turns number into a list of its digits
    digits = [int(k) for k in str(num)]
    return digits

def convert(list): #turns digit list into a number
    num = sum(digit * pow(10,i) for i, digit in enumerate(list[::-1]))
    return (num)

def pandigital_check(num):
    digits = deconstruct(num)
    if sorted(digits) == [1,2,3,4,5,6,7,8,9]:
        return True
    else:
        return False

def concat_product(integer):
    for k in range(2,10):
        digits = []
        num_list = list(range(1,k))
        for num in num_list:
            product = num * integer
            for i in deconstruct(product):
                digits.append(int(i))
        if pandigital_check(convert(digits)) is True:
            pandigital_products.append(convert(digits))
        if len(digits) > 9:
            break

for j in range(2 ,10000):
    concat_product(j)

answer = max(pandigital_products)

print(answer)