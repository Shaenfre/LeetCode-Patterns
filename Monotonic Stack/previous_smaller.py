def previous_smaller(nums):
    """
    Strictly Increasing
    """
    N = len(nums)
    stack, previous_smaller = [], [-1] * N

    for i in range(N):
        while stack and nums[stack[-1]] > nums[i]:
            stack.pop()

        if stack:
            previous_smaller[i] = nums[stack[-1]]

    return previous_smaller
