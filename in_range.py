def in_range(nums, lowest, highest):
    for num in range(len(nums)):
        if (nums[num] > lowest) and (nums[num] < highest + 1): 
          print(str(nums[num]) + " fits")

in_range([10, 20, 30, 40, 50], 15, 30)            
