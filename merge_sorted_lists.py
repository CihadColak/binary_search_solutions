def solve(a, b):
    l_index = 0
    r_index = 0
    merged_list = []
    while l_index < len(a) and r_index < len(b):
        # compare number at l_i and r_i
        if a[l_index] <= b[r_index]:
            merged_list.append(a[l_index])
            l_index += 1
        else:
            merged_list.append(b[r_index])
            r_index += 1
    return merged_list + a[l_index:] + b[r_index:]


a = [5, 10, 15, 16, 19, 21, 22]

b = [3, 8, 9, 11, 12, 15, 17]
print(solve(a, b))
