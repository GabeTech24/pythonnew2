print("Good day wonderful customer!")
print("We'd like to give you an actual breakdown of the discount you get from us.")
print("Kindly Enter the Price of the good you bought below:")

purchase_amount = int(input('Purchase Price of Goods Bought in ($): '))
print(f'Your purchase Price is ${purchase_amount}')
if purchase_amount < 100:
    discount = 0
    print(f'Your discount is ${discount:.2f}')
elif 100 >= purchase_amount <= 500:
    discount = 0.1 * purchase_amount
    print(f'Your discount is ${discount:.2f}')
elif purchase_amount > 500:
    discount = 0.2 * purchase_amount
    print(f'Your discount is ${discount:.2f}')
else:
    print('No Discount given')

actual_purchase_price = purchase_amount - discount
if discount >= 0:
    print (f'Your actual Purchase Price (after Discount) is ${actual_purchase_price:.2f}')

print ("Now's let's calculate your tax:")
x = int(input("Enter your discounted amount in $: "))
if x < 200:
    tax = 0.05 * actual_purchase_price
    print (f"The tax deduction on the discount you were given is ${tax:.2f}")
elif x > 200:
    tax = 0.08 * actual_purchase_price
    print (f"The tax deduction on the discount you were given is ${tax:.2f}")
else:
    print('No Tax deduction made')
final_purchase_amount = tax + actual_purchase_price
print(f'Original purchase amount of the customer ($):{purchase_amount:.2f} ')
print(f'Discount applied ($):{discount:.3f} ')
print(f'Tax applied ($):{tax:.3f}')
print(f'Final amount the customer paid ($):{final_purchase_amount:.2f} ')
print('Thanks a lot')