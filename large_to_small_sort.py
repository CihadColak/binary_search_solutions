def solve(nums):
    res = []
    rest_of_list = nums
    while len(res) != len(nums):
        curr_max = rest_of_list[0]
        curr_max_index = 0
        curr_min = rest_of_list[0]
        curr_min_index = 0
        for i, v in enumerate(rest_of_list):
            if v > curr_max:
                curr_max = v
            if v < curr_min:
                curr_min = v
        res.append(curr_max)
        rest_of_list.remove(curr_max)
        res.append(curr_min)
        rest_of_list.remove(curr_min)
    return res


print(solve([3, 1, 2, 4]))
