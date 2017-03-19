magicNumber = 100
for n in range(101):
    if n is magicNumber:
        print(n,"is mage number")
        break
    else:
        print(n)

number = 10 
for n in range(12):
    if n is number:
        continue
    else:
        print(n,"not number")      