def number(high, low):
    for i in range(high, low+1):
        flag =0
        for j in range(2, i):
            if (i%j)==0:
                flag=1
                break

        if flag==0:
            print (i , end = ' ')

number(3,11)
