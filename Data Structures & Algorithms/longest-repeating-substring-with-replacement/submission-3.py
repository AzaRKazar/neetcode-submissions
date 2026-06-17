class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #brute:
        result=0
        # for i in range(len(s)):
        #     count, max_freq={},0
        #     for j in range(i,len(s)):
        #         count[s[j]]=count.get(s[j],0)+1
        #         max_freq=max(count[s[j]],max_freq)
        #         if (j-i+1)-max_freq<=k:
        #             result=max(result,j-i+1)
        # return result
        
        
        
        
        #optimal
        # left=0
        # max_freq=0
        # max_length=0
        # count={}#hashmap or dict
        # for right in range (len(s)):
        #     char=s[right]
        #     count[char]=count.get(char,0)+1
        #     max_freq=max(max_freq,count[char])
        #     while (right-left+1)-max_freq>k:
        #         count[s[left]]-=1
        #         left+=1
        #     max_length=max(max_length,(right-left+1))
        # return max_length


        left=0
        hashmap={}
        length=0
        max_freq=0
        max_length=0
        for right in range(len(s)):
            hashmap[s[right]]=hashmap.get(s[right],0)+1
            max_freq=max(hashmap[s[right]],max_freq)
            while(right-left+1)-max_freq>k:
                hashmap[s[left]]-=1
                left+=1
            max_length=max(max_length,(right-left+1))
        return max_length

            





