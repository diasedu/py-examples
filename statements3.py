a = 200
b = 33
c = 500

if a > b and c > a:
    print("Both conditions are true")

if a > b or c > a:
    print("A least one of the conditions is true")

c = 1
d = 2

if not c > d:
    print("c is NOT greater than d")