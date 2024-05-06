# 0965 - Unique Email Addresses
# Date: 2024-05-05
# Runtime: 80 ms, Memory: 16.6 MB
# Submission Id: 1249943483


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            n = len(email)
            chars = []
            has_at = False
            for i in range(n):
                if email[i] == '@':
                    chars.append(email[i:])
                    break
                if has_at or email[i] == '.':
                    continue
                elif email[i] == '+':
                    has_at = True
                    continue
                chars.append(email[i])

            unique.add(''.join(chars))

        return len(unique)