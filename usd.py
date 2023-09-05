a=input()
def reversed1(variable):
        res = ''
        for i in range(len(variable) - 1, -1, -1):
            res += variable[i]
        return res

n = reversed1(a)
print(n)
print(a)
if a==n:
    print(True)
else:
    print(False)