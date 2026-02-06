def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print("NWD(48, 18) =", nwd(48, 18))
print("NWD(100, 35) =", nwd(100, 35))
print("NWD(17, 13) =", nwd(17, 13))
print("NWD(0, 5) =", nwd(0, 5))
print("NWD(0, 0) =", nwd(0, 0))    

"""

"""
