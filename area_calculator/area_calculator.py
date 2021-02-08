def area_triangle(b, h):
    result = 1 / 2 * b * h
    print("The area is: ", result)

def area_rectangle(l, w):
    result = l * w
    print("The area is: ", result)

def area_square(s):
    result = s * 2
    print("The area is: ", result)

def area_circle(r):
    result = 3.14 * r * 2
    print("The area is: ", result)


print("Shape Area Calculator")
print()
print("-=-==-=-=-==-=-=-=-=-=-=-=-==")
print()
print("1. Triangle")
print("2. Rectangle")
print("3. Square")
print("4. Circle")
print("5. Quit")
print()

shape = input("Which Shape: ")

if shape is '1':
    b = int(input("Base: "))
    h = int(input("Height: "))
    area_triangle(b, h)
elif shape is '2':
    l = int(input("Length: "))
    w = int(input("Width: "))
    area_rectangle(l, w)
elif shape is '3':
    s = int(input("Side: "))
    area_square(s)
elif shape is '4':
    r = int(input("Radius: "))
    area_circle(r)
elif shape is '5':
    quit()
else:
    print("input error")