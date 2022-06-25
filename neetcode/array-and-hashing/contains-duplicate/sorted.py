def containsDuplicate(nums):
    sorted_nums = sorted(nums)
    prev = None

    for num in sorted_nums:
        if num == prev:
            return True
        prev = num
    return False

