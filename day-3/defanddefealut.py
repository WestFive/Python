def get_gender(sex='Unknown'): #defalut = Unknown
    if sex is'm':
        sex="Male"
    elif sex is 'f':
        sex='female'
    print(sex)
get_gender('m')
get_gender('f')
get_gender()