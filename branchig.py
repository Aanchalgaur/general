def username(name):
    if len(name) < 3:
        print(" the length is too short try again")
    else:
        print (name)

username("hi")

username("aanchsj")

def even_number(number):
    if number %2 ==0:
        print("true")
    return False

even_number(5)


def username(name):
    if len(name) < 3:
        print("invalid username")
    elif len (name) > 15:
        print("username too long")
    else:
        print("valid username" + name)

username("hiedkejddhejdekjdkjdeijedejfhjehfjef")
username("hibecky")