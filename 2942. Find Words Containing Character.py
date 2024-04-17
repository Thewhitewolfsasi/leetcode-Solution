class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        out = []
        for i, value in enumerate(words):
            if x in value:
                out.append(i)
        return out
        
