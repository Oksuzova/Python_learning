# while True:
#     try:
#         price = float(input('Enter your price:'))
#         if price >= 0:
#             print('tax = 18%')
#             tax = price * 0.18
#             print(f'tax = {tax}')
#             print('tip = 10%')
#             tip = price * 0.10
#             print(f'tip = {tip}')
#             full_price = price + tax + tip
#             print(f'Full = {full_price}')
#             break
#         else:
#             print('Error')
#     except ValueError:
#         print('Please,enter your price')
#

# def unique(list1):
#     unique_list = []
#     for x in list1:
#         if x not in unique_list:
#             unique_list.append(x)
#     print(unique_list)
#
# list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# print("unique")
# unique(list1)
#
# list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# print("unique")
# unique(list2)

s = "ab,abc,ab,a"


def words(text):
    words = text.split(",")
    quant = {k: words.count(k) for k in words}
    maxim = max(quant, key=quant.get)
    longest = max(words, key=len)
    return f"{longest} {maxim}"


print(words(s))



