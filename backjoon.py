n = int(input())

def aa(n, counts = 0):
    if n == 1:
        return counts
    elif n % 3 == 0:
        n = n // 3
        counts += 1
        return aa(n, counts)
    elif n % 2 == 0:
        n = n // 2
        counts += 1
        return aa(n, counts)
    else:
        n -= 1
        counts += 1
        return aa(n, counts)

def aaa(n):
    
print(aa(n))