class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        arrows = 1
        curr_point = points[0]
        for point in points:
            if curr_point[1] < point[0]:
                curr_point = point
                arrows += 1
        return arrows
        