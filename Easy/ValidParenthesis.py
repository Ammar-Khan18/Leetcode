# Valid Parenthesis
s = "]"

pairs = {')': '(', ']': '[', '}': '{'}
stack = []
valid = True

for ch in s:
    if ch in pairs.values():
        stack.append(ch)
    elif ch in pairs:
        if not stack or stack[-1] != pairs[ch]:
            valid = False
            break
        stack.pop()
    else:
        continue

if valid and not stack:
    print(True)
else:
    print(False)
