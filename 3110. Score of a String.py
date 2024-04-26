class Solution:
    def scoreOfString(self, s: str) -> int:
        #remove last values
        s1 = s[:-1]
        # print(type(ord(s[1])))
        out = 0
        for i in range(len(s1)):
            out += abs(ord(s[i])-ord(s[i+1]))
        return out
