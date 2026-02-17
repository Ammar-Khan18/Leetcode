# Valid Parenthesis
s = "]"  # sample input; change as needed

# use a mapping from closing to opening characters
pairs = {')': '(', ']': '[', '}': '{'}
stack = []
valid = True

for ch in s:
    if ch in pairs.values():
        # opening bracket
        stack.append(ch)
    elif ch in pairs:
        # closing bracket: must match the top of the stack
        if not stack or stack[-1] != pairs[ch]:
            valid = False
            break
        stack.pop()
    else:
        # ignore any other character (not needed for LeetCode)
        continue

# final result is True iff no invalid condition was seen and stack is empty
if valid and not stack:
    print(True)
else:
    print(False)
