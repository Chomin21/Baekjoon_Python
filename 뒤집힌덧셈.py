X, Y = map(int, input().split())

def Rev(m):
    m = str(m)
    k = ""
    for i in range(0, len(m)):
        k += m[len(m) - 1 - i]
    return int(k)

print(Rev(Rev(X) + Rev(Y)))