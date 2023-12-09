print("Enter a number to find the nth rarest item:")
index_list = [2, 7, 3, 5, 4, 4, 3, 5, 2, 2, 3]
nth = int(input("Enter a positive integer: "))


def nth_most_rare(lst, n):
    freq_dict = {}
    for num in lst:
        freq_dict[num] = freq_dict.get(num, 0) + 1

    sorted_freq = sorted(freq_dict.items(), key=lambda x: x[1])

    if 1 <= n <= len(sorted_freq):
        nth_rarest_item = sorted_freq[-n][0]
        return nth_rarest_item
    else:
        return None
    

result = nth_most_rare(index_list, nth)
if result is not None:
    print(f"The {nth}nd rarest item is: {result}")
else:
    print("Invalid input. Please enter a valid positive integer.")