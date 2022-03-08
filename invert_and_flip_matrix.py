def flip_row(row):
    flipped_row = [0 if x == 1 else 1 for x in row]
    return flipped_row


print(flip_row([1, 0, 0, 1]))
