
def noRepeat(string):
    window_start = 0
    word_set = {}
    longest_distinct_length = -float('inf')

    for window_end in range(len(string)):
        char = string[window_end]

        if char in word_set:
            window_start = max(window_start, word_set[char] + 1)

        word_set[char] = window_end
        longest_distinct_length = max(longest_distinct_length, window_end - window_start + 1)

    return longest_distinct_length

for  string in ['aabccbb', 'abbbb', 'abccde']:
    print(noRepeat(string)) 
