s = "MCMXCIV"
res = 0
i = 0
after = 2
while i < len(s):
    if s[i:after] == "IV":
        res += 4
        i += 2
        after += 2
    elif s[i:after] == "IX":
        res += 9
        i += 2
        after += 2
    elif s[i:after] == "XL":
        res += 40
        i += 2
        after += 2
    elif s[i:after] == "XC":
        res += 90
        i += 2
        after += 2
    elif s[i:after] == "CD":
        res += 400
        i += 2
        after += 2
    elif s[i:after] == "CM":
        res += 900
        i += 2
        after += 2
    elif s[i] == 'I':
        res += 1
        i += 1
        after += 1
    elif s[i] == 'V':
        res += 5
        i += 1
        after += 1
    elif s[i] == 'X':
        res += 10
        i += 1
        after += 1
    elif s[i] == 'L':
        res += 50
        i += 1
        after += 1
    elif s[i] == 'C':
        res += 100
        i += 1
        after += 1
    elif s[i] == 'D':
        res += 500
        i += 1
        after += 1
    elif s[i] == 'M':
        res += 1000
        i += 1
        after += 1
print(res)
