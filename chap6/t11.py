def fac(a):
    if a==1:
        return 1
    else:
        res = a*fac(a-1)
        return res
print(fac())