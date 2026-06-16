class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #brute
        result=0
        for i in range(len(s)):
            seen=set()
            for j in range(i,len(s)):
                # if s[j] in seen:
                #     break
                # seen.add(s[j]) this also works 
                if s[j] not in seen:
                    seen.add(s[j])
                else:
                    break
            result=max(result,len(seen))
        return result    
#        optiaml
        seen=set()
        left=0
        max_length=0
        for right in range(len(s)):
            while s[right]in seen:
                seen.remove(s[left]) 
                left+=1
            seen.add(s[right])
            max_length=max(max_length,len(seen))
        return max_length
