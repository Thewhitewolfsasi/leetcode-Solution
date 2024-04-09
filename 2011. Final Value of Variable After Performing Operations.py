class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        out = 0
        for i in operations:
            if i == "++X" or i=="X++":
                out += 1
            elif i == '--X' or i=='X--':
                out -= 1
        return out
        
