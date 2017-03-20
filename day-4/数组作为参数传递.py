def health_calculator(age,appls_ate,cigs_somoked):
    answer = (100-age)+(appls_ate * 3.5) -(cigs_somoked * 2)
    print(answer)

bucys_data = [27,20,0]

health_calculator(bucys_data[0],bucys_data[1],bucys_data[2])

#实际上传入一个列表并标记就行了
health_calculator(*bucys_data)