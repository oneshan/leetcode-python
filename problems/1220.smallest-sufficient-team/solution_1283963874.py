# 1220 - Smallest Sufficient Team
# Date: 2024-06-10
# Runtime: 410 ms, Memory: 118 MB
# Submission Id: 1283963874


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(people)
        m = len(req_skills)
        
        skill_id = {skill: idx for idx, skill in enumerate(req_skills)}
        people_skills = [0] * n
        for idx, skills in enumerate(people):
            for skill in skills:
                people_skills[idx] |= (1 << skill_id[skill])

        final_mask = (1 << m) - 1

        @cache
        def dp(i, team_skills):
            if team_skills == final_mask:
                return 0
            if i == len(people):
                return (1 << 61) - 1
            
            skip = dp(i+1, team_skills)
            pick = (1 << i) | dp(i+1, team_skills | people_skills[i])
            return pick if pick.bit_count() < skip.bit_count() else skip

        return [i for i in range(n) if dp(0, 0) & (1 << i)]