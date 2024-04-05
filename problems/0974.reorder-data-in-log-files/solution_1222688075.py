# 0974 - Reorder Data in Log Files
# Date: 2024-04-04
# Runtime: 42 ms, Memory: 16.6 MB
# Submission Id: 1222688075


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        def get_id(log):
            identifier, content = log.split(' ', 1)
            if content[0].isdigit():
                return (1, )
            return (0, content, identifier)

        return sorted(logs, key=get_id)