def next_prev_greater(nums):
    """
    Monotonically decreasing stack
    """
    N = len(nums)
    stack, next_greater, prev_greater = [], [-1] * N, [-1] * N

    for i in range(N):
        while stack and nums[stack[-1]] < nums[i]:
            next_greater[stack.pop()] = nums[i]

        if stack:
            """
            here previous greater may be equal to current element
            to make strictly greater replace < above with <= (strictly decreasing stack)
            """
            prev_greater[i] = nums[stack[-1]]

        stack.append(i)

    return next_greater