# 2429 - Design a Food Rating System
# Date: 2023-12-17
# Runtime: 916 ms, Memory: 46.2 MB
# Submission Id: 1121609173


from sortedcontainers import SortedList
from collections import defaultdict

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisines = defaultdict(SortedList)
        self.food_data = {}
        
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_data[food] = (cuisine, rating)
            self.cuisines[cuisine].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, rating = self.food_data[food]
        self.food_data[food] = cuisine, newRating
        self.cuisines[cuisine].remove((-rating, food))
        self.cuisines[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.cuisines[cuisine][0][1]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)