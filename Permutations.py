def permute(nums):

    result = []

    def dfs(path, remaining):

        if not remaining:
            result.append(path)

        for i in range(len(remaining)):

            dfs(
                path + [remaining[i]],
                remaining[:i] + remaining[i+1:]
            )

    dfs([], nums)

    return result


print(permute([1,2,3]))