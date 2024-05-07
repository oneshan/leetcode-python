# 0271 - Encode and Decode Strings
# Date: 2024-05-06
# Runtime: 71 ms, Memory: 16.9 MB
# Submission Id: 1250826770


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = []
        for s in strs:
            res.append(f'{len(s)}#{s}')
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        while i < len(s):
            size = 0
            while s[i] != '#':
                size = 10 * size + int(s[i])
                i += 1
            i += 1
            res.append(s[i:i+size])
            i += size
        return res



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))