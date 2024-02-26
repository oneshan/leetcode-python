# 1220 - Smallest Sufficient Team
# Date: 2023-07-16
# Runtime: 576 ms, Memory: 21.6 MB
# Submission Id: 995565007


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(people)
        m = len(req_skills)
        
        skill_id = {skill: idx for idx, skill in enumerate(req_skills)}
        skill_mask = [0] * n
        for idx, skills in enumerate(people):
            for skill in skills:
                skill_mask[idx] |= (1 << skill_id[skill])
                
        @cache
        def dfs(mask):
            if mask == 0:
                return 0
            
            result = (1 << n) - 1
            for i in range(n):
                new_mask = mask & ~skill_mask[i]
                if new_mask != mask:
                    p_mask = dfs(new_mask) | (1 << i)
                    if p_mask.bit_count() < result.bit_count():
                        result = p_mask
            return result
        
        ans_mask = dfs((1 << m)-1)
        ans = []
        for i in range(n):
            if ans_mask & 1:
                ans.append(i)
            ans_mask >>= 1
            
        return ans