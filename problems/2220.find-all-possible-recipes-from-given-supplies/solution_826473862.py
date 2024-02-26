# 2220 - Find All Possible Recipes from Given Supplies
# Date: 2022-10-20
# Runtime: 998 ms, Memory: 17.3 MB
# Submission Id: 826473862


from collections import defaultdict, deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(set)
        in_degree = defaultdict(int)
        
        for recipe, ingredient in zip(recipes, ingredients):
            for item in ingredient:
                graph[item].add(recipe)
            in_degree[recipe] = len(ingredient)
            
        ans = []
        queue = deque(supplies)
        while queue:
            item = queue.popleft()
            if item in recipes:
                ans.append(item)
            for neighbor in graph[item]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return ans