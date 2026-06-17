class Solution:

    def encode(self, strs: List[str]) -> str:
        encode=[]
        for i in range(len(strs)):
            length=len(strs[i])
            encode.append(f"{length}#{strs[i]}")
        return "".join(encode)
    def decode(self, s: str) -> List[str]:
        result=[]
        i=0

        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1

            length=int(s[i:j])
            word=s[j+1:j+1+length]
            result.append(word)

            i=j+1+length

        return result