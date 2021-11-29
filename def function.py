def greeting(name):
    print("hello, " + name)

greeting("namya")
greeting("shreya")

def greeting(name, department):
    print("welcome, " + name)
    print("your department is, " + department)

greeting("aliya", "freezone")


def get_seconds(hours, minutes, seconds):
    return 3600*hours + 60*minutes + seconds

amount_a= get_seconds(2,5,0)
amount_b= get_seconds(0, 5, 45)
result = amount_b + amount_a

print(result)

print( 5//2)

def convert_seconds(second):
    hours = second//3600
    minutes = (second- hours * 3600)//60
    remaining_seconds= second - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds
hours, minutes, second = convert_seconds(4009)
print(hours, minutes, second)

def lucky_number(name):
    number = len(name)*9
    print("hello," +name +"your lucky number is" + str(number))

lucky_number("booch")

def rectangle_area(base, height):
    area = base* height
    print("the area is " + str(area))

rectangle_area(4, 4)




