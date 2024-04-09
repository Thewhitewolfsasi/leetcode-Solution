class Solution:
    def defangIPaddr(self, address: str) -> str:
        out=""
        for i in address:
            out += i
            if i == ".":
                out = out[:-1] + "[" + i + "]"
        return out
