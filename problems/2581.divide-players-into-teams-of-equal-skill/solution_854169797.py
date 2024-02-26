# 2581 - Divide Players Into Teams of Equal Skill
# Date: 2022-12-04
# Runtime: 579 ms, Memory: 27.7 MB
# Submission Id: 854169797


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        ans = 0
        left, right = 0, len(skill)-1
        equal = skill[left] + skill[right]
        while left < right:
            two_sum = skill[left] + skill[right]
            if two_sum != equal:
                return -1
            ans += skill[left] * skill[right]
            left += 1
            right -= 1
        return ans