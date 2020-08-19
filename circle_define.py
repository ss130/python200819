def circle_area(x):
    num=x*x*3.14
    return num
def circle_circum(a):
    num=a*2*3.14
    return num

n=int(input("半徑:"))
z=circle_area(n)
a=circle_circum(n)
print("圓面積",z,"圓周",a)
