class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result=[]
        largestval=max(candies)#taking max val for refernce
        for i in range(len(candies)):
            if candies[i] + extraCandies >=largestval:
                result.append(True)
            else:
                result.append(False)
        return result
