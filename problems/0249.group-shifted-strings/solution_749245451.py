# 0249 - Group Shifted Strings
# Date: 2022-07-17
# Runtime: 83 ms, Memory: 13.9 MB
# Submission Id: 749245451


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        def get_hash(string: str) -> str:
            first = string[0]
            return ' '.join(chr((ord(ch)-ord(first)) % 26) for ch in string)
            
        table = {}
        for string in strings:
            key = get_hash(string)
            table.setdefault(key, [])
            table[key].append(string)
        return table.values()