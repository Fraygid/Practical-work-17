def solve(a,b,c):
    d = b**2 - 4*a*c

    x1 = (-b+d**0.5)/(2*a)
    x2 = (-b-d**0.5)/(2*a)

    return min(x1,x2), max(x1,x2)

print(solve(1, -4, -5))
print(solve(-2, 7, -5))
print(solve(1, 2, 1))
