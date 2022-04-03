

def slide(month, vacay_len):
    len_list = len(month)
    if len_list < vacay_len:
        print("Invalid Selection - Vacation too long")
        return -1
    window_sum = sum(month[:vacay_len])
    max_sum = window_sum
    for i in range(len_list - vacay_len):
        window_sum = window_sum - month[i] + month[i + vacay_len]
        max_sum = max(window_sum, max_sum)
        if max_sum == window_sum:
            vacay_start = i
            vacay_end = i + vacay_len
    return max_sum, vacay_start, vacay_end
