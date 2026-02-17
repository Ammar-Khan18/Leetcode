x = 121
false = 0
true = 0
for i in range(0, len(str(x))):
    if str(x)[i] != str(x)[len(str(x)) - 1 - i]:
        false += 1
    elif str(x)[i] == str(x)[len(str(x)) - 1 - i]:
        true += 1
if false > 0:
    print(False)
else:
    print(True)
