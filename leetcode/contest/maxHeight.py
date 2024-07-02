# https://leetcode.com/problems/maximum-height-of-a-triangle/description/

def maxHeightOfTriangle(red, blue):
    def helper(ball_1, ball_2):
        height = 0
        i = 1
        
        while True:
            if i % 2:
                if ball_1 >= i:
                    ball_1 -= i
                else:
                    break
            else:
                if ball_2 >= i:
                    ball_2 -= i
                else:
                    break

            
            height += 1
            i += 1

        return height

    return max(helper(red, blue), helper(blue, red))

red = 2
blue = 4
print(maxHeightOfTriangle(red, blue))