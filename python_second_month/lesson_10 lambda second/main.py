# 1

result = lambda a,b: print((a**2) + (b**2))
result(6, 5)

# 2

def inputelement(text: str, num: int):
    textcount = 0
    for i in text:
        if i in 'aeuio':
            textcount += 1
    print(textcount * num)

inputelement('adham', 7)

# 3

def maxnum(a: int, b: int, c: int):
    if a > b and a > c:
        print(f"{a} eng katta son")
    elif b > a and b > c:
        print(f"{b} eng katta son")
    else:
        print(f"{c} eng katta son")

maxnum(5, 6, 8)

# 4

def pluslement(text: str, num: int):
    textcountm = 0
    textcountp = 0
    for i in text:
        if i in 'qwrtypsdfghjklzxcvbnm':
            textcountm += 1
        if i in 'aueio':
            textcountp += 1   
    print((textcountm - textcountp) + num)

pluslement('adham', 9)


# 5
numlist = []

def maximumandlist(a: int, c: int, d: int, e: int, f: int):
    numlist.append(max(a, c, d, e, f))

maximumandlist(5, 8, 4, 6, 3)
print(numlist)