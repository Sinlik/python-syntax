def any7(nums):
    for val in range(len(nums)):
        if int(nums[val]) == 7:
            return True
print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

