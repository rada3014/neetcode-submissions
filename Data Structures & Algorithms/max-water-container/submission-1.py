class Solution:
    def maxArea(self, heights: List[int]) -> int:

        start = 0
        end = len(heights)-1
        highest_area = 0

        while (start<end):

            width = end-start
            height = min(heights[start],heights[end])

            area = height*width

            #print(width,height,area)

            if area>highest_area:
                highest_area=area

            
            if heights[end]>heights[start]:
                start= start+1

            else:
                end = end-1
        return highest_area
        