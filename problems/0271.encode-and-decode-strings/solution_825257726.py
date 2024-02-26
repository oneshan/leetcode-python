# 0271 - Encode and Decode Strings
# Date: 2022-10-18
# Runtime: 148 ms, Memory: 14.2 MB
# Submission Id: 825257726


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return ''.join(f'{len(s)}#{s}' for s in strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        ans = []
        while s:
            length, s = s.split('#', 1)
            token, s = s[:int(length)], s[int(length):]
            ans.append(token)
        return ans

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))