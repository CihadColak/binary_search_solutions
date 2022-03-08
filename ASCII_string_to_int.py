class Solution:
    def solve(self, s):
        curr_s = ""
        count = 0
        for c in s:
            if c.isnumeric():
                curr_s += c
            else:
                count += int(curr_s)
                curr_s = "0"
        return count

    print(solve(1, "11aa23bb5"))
