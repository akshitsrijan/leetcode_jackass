class Solution:
    def nextGreaterElement(self, nums1, nums2):

        stack = []
        next_greater = {}

        for num in nums2:
            while stack and stack[-1] < num:
                smaller = stack.pop()
                next_greater[smaller] = num
            stack.append(num)

        # Remaining elements have no greater element
        for num in stack:
            next_greater[num] = -1

        # Build result
        return [next_greater[num] for num in nums1]
