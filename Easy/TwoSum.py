# Solution 1: Brute Force (Worked but not efficient enough)
nums = [2, 7, 11, 15]
target = 9
ind1 = 0
ind2 = 0
result = []
for i in range(len(nums)):
    for j in range(len(nums)-1):
        if nums[j] + nums[i] == target:
            ind1 = i
            ind2 = j
            break
result.append(ind2)
result.append(ind1)
print(result)
# --------------------------------------------------------
# Solution 2: Recursive (FAILED DUE TO RECURSION LIMIT)
# result = []
# i = 0
# j = 0
# nums = [2, 7, 11, 15]
# target = 9

# def foo(nums, target, i, j, result=[]):
#     if (nums[i] + nums[j] == target) and (i != j):
#         result.append(i)
#         result.append(j)
#         return result
#     elif j == len(nums)-1:
#         i = i + 1
#         j = 0
#         return foo(nums, target, i, j, result)
#     else:
#         j = j + 1
#         return foo(nums, target, i, j, result)


# res = foo(nums, target, i, j, result)
# print(res)
# --------------------------------------------------------