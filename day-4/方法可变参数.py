def add_numbers(*args):#可变参数
    total= 0
    for a in args:
        total +=a 
    print(total)

add_numbers(3)
add_numbers(3,4,5)
