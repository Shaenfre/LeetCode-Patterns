"""
Strictly decreasing stack
"""


def previousGreater(nums):
    N = len(nums)
    stack, previousGreater = [], [-1] * N

    for i in range(N):
        while stack and nums[stack[-1]] < nums[i]:
            stack.pop()

        if stack:
            previousGreater[i] = nums[stack[-1]]

        stack.append(i)

    return previousGreater
