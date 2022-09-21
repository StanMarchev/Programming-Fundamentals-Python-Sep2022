# budget = int(input())
# command = input()
#
# while command != 'End':
#     product_price = int(command)
#     budget -= product_price
#
#     if budget < 0 :
#         print('You went in overdraft!')
#         break
#     command = input()
# else:
#     print('"You bought everything needed.')
budget = int(input())
command = input()  # either "End" or price
budget_is_enough = True
while command != "End":
    price = int(command)
    if budget >= price:
        budget -= price
    else:  # if price > budget
        budget_is_enough = False
        print("You went in overdraft!")
        break
    command = input()
if budget_is_enough:
     print("You bought everything needed.")