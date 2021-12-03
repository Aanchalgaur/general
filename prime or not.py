num= int(input("enter your number"))

if num>1:
    for i in range(2,int(num/2)+1):
        if(num%i) == 0:
            print("not prime")
            break
        else:
            print("is prime")

else:
    print("not prime")





