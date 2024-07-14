# 0726 - Number of Atoms
# Date: 2024-07-14
# Runtime: 32 ms, Memory: 16.7 MB
# Submission Id: 1320170041


class Solution:
    def countOfAtoms(self, formula: str) -> str:

        stack = [1]
        counter = Counter()
        atom, cnt = '', ''

        for ch in formula[::-1]:
            if ch.isdigit():
                cnt = ch + cnt
            elif ch == ')':
                stack.append(int(cnt) * stack[-1] if cnt else 1)
                cnt = ''
            elif ch == '(':
                stack.pop()
                cnt = ''
            elif ch.islower():
                atom = ch
            else:
                atom = ch + atom
                counter[atom] += stack[-1] * (int(cnt) if cnt else 1)
                atom, cnt = '', ''
        
        res = []
        for atom in sorted(counter):
            if counter[atom] == 1:
                res.append(atom)
            else:
                res.append(f'{atom}{counter[atom]}')

        return ''.join(res)