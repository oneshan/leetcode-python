# 0965 - Unique Email Addresses
# Date: 2022-11-23
# Runtime: 276 ms, Memory: 13.9 MB
# Submission Id: 848593145


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        for email in emails:
            names = []
            with_plus = False 
            for idx, ch in enumerate(email):
                if ch == '.':
                    continue
                if ch == '+':
                    with_plus = True
                if not with_plus and ch != '@':
                    names.append(ch)
                if ch == '@':
                    names.append(email[idx:])
                    break
            ans.add(''.join(names))
        return len(ans)