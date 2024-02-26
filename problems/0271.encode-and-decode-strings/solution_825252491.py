# 0271 - Encode and Decode Strings
# Date: 2022-10-18
# Runtime: 152 ms, Memory: 14.1 MB
# Submission Id: 825252491


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return f'{len(strs)}\t' + '\t'.join(strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        length, *strs = s.split('\t')
        return [] if length == '0' else strs
        
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))