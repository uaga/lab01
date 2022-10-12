def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


x = int(input("A = "))
y = int(input("B = "))
num = gcd(x, y)

print("НОД(A,B) = ")
print(num)
