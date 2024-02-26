# 0965 - Unique Email Addresses
# Date: 2023-08-02
# Runtime: 87 ms, Memory: 16.4 MB
# Submission Id: 1010384720


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        
        for email in emails:
            chars = []
            with_plus = False
            for idx, ch in enumerate(email):
                if ch == '.':
                    continue
                if ch == '+':
                    with_plus = True
                if ch == '@':
                    chars.append(email[idx:])
                    break
                if not with_plus:
                    chars.append(ch)
            ans.add(''.join(chars))
        
        return len(ans)