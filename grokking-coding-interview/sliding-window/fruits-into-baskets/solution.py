def pickFruits(array, num_of_baskets):

    window_start = 0
    baskets_pool = {}
    total_fruits = -float('inf')

    for window_end in range(len(array)):
        char = array[window_end]

        baskets_pool[char] = baskets_pool.setdefault(char, 0) + 1

        while(len(baskets_pool) > num_of_baskets):
            begining_char = array[window_start]
            if(baskets_pool[begining_char] == 1):
                del baskets_pool[begining_char]
            else:
                baskets_pool[begining_char] -= 1
            window_start += 1
        total_fruits = max(total_fruits, window_end - window_start + 1)
    return total_fruits


print(pickFruits(['A', 'B', 'C', 'A', 'C'], 2))
print(pickFruits(['A', 'B', 'C', 'B', 'B', 'C'], 2))
