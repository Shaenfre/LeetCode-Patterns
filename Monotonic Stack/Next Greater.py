def next_greater(nums):
    """
    Monotonically decreasing stack
    """
    N = len(nums)
    stack, next_greater = [], [] * N

    for i in range(N):
        while stack and nums[stack[-1]] < nums[i]:
            next_greater[stack.pop()] = nums[i]

        stack.append(i)

    return next_greater