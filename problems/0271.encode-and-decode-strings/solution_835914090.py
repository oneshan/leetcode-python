# 0271 - Encode and Decode Strings
# Date: 2022-11-03
# Runtime: 201 ms, Memory: 14.2 MB
# Submission Id: 835914090


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return ''.join(f'{len(s)}#{s}' for s in strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        strs = []
        while s:
            length, s = s.split('#', 1)
            token, s = s[:int(length)], s[int(length):]
            strs.append(token)
        return strs

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))