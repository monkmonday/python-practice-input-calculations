#Practice 1
length = int(input('enter the length of rectangele in cm : '))
breath = int(input('enter the breath of rectangele in cm : '))
print(length)
print(breath)
area = length*breath
print(f"the area is {area} cm²")

#Practice 2
item = input("what Item are you buying? :")
price = float(input(f'What is the price of {item} ? :'))
Quantity = int(input(f'How Many {item} are you Buying? : '))

total = price*Quantity
print(f"You Have Bought {Quantity} X {item}/s")
print(f"Your Total is : ${total}")