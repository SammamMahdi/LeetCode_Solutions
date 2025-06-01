class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # for i in range(1, x + 1):

        #     if i * i == x:
        #         return i
        #     elif i * i > x:
        #         return i - 1
        # return x
        right = x
        left = 0
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return right

