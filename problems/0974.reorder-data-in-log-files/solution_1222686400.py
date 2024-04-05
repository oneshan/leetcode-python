# 0974 - Reorder Data in Log Files
# Date: 2024-04-04
# Runtime: 51 ms, Memory: 16.7 MB
# Submission Id: 1222686400


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        table = defaultdict(list)
        
        letter_logs = []
        digit_logs = []
        for log in logs:
            identifier, content = log.split(' ', 1)
            if content[0].isdigit():
                digit_logs.append(log)
            else:
                table[content].append(identifier)

        for content in sorted(table.keys()):
            for identifier in sorted(table[content]):
                letter_logs.append(f'{identifier} {content}')

        return letter_logs + digit_logs