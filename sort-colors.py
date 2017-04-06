'''
Given an array with n objects colored red, white, or blue
sort them so that objects othe same color are adjacent, with the colors
in the order red, white and blue

use 0, 1, 2 to represent red, white and blue

Given [1, 0, 1, 2] , sort in place to [0, 1, 1, 2]

'''
class Solution:
    def sort(self, A, flag, index):
        start, end = index, len(A) - 1
        while start <= end:
            while start <= end and A[start] == flag:
                start += 1
            while start <= end and A[end] != flag:
                end -= 1
            if start <= end:
                A[start], A[end] = A[end], A[start]
                start += 1
                end -= 1
        return start

    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        self.sort(A, 1, self.sort(A, 0, 0))

s = Solution()
a=[2,0,0,1,2,0,2]
print(s.sortColors(a))
