def next_smaller(nums: list[int]):
    """
    Strictly Increasing
    """
    N = len(nums)
    stack, next_smaller = [], [-1] * N

    for i in range(N):
        while stack and nums[i] < nums[stack[-1]]:
            next_smaller[stack.pop()] = nums[i]

        stack.append(i)

    return next_smaller
