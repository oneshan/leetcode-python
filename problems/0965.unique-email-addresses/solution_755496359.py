# 0965 - Unique Email Addresses
# Date: 2022-07-24
# Runtime: 77 ms, Memory: 14 MB
# Submission Id: 755496359


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.replace('.', '').split('+')[0]
            ans.add(f'{local}@{domain}')
        return len(ans)