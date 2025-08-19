class Solution(object):
    def maxArea(self, height):
        maxarea=0
        left=0
        right=len(height)-1
        while left<right:
            width=right-left
            length=min(height[left],height[right])
            maxarea=max(maxarea,length*width)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxarea

        