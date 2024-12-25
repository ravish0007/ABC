


def combination(nums, target):

    res = []


    def dfs(i, cur, total):

        if target == total:
            res.append(cur)
            return

        if total > target or i >= len(nums):
            return

        cur.append(nums[i])
        dfs(i, cur, total+nums[i])

        cur.pop()
        dfs(i+1, cur, total)

    dfs(0, [], 0)
    return res
