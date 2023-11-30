class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        sum=""
        Remainder=""
        if(len(word1)< len(word2)):
            Remainder=word2[len(word1):]
        elif(len(word1)>len(word2)):
            Remainder=word1[len(word2):]
        
        for i in range(min(len(word1),len(word2))):
            sum+= word1[i]
            sum+= word2[i]
        sum+=Remainder
        return sum
