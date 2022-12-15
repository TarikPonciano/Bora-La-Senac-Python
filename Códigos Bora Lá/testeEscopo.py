def f1 (x):
    a = 10
    print(x + a)

def f2 (x):
    num = 10
    print(x+num)

def f3 (x):
    global num
    num = 10
    print(x+num)

num = 20

f1(num)

f2(num)

f3(num)

print(num)