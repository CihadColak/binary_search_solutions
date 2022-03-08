def solve(nums, k, target):
    nums_sum = sum(nums)
    counter = 0
    if target == nums_sum:
        return counter
    if target < nums_sum:
        while target < nums_sum:
            nums_sum += k
            counter += 1
        return counter
    else:
        while target > nums_sum:
            nums_sum -= k
            counter += 1
        return counter
