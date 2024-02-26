# 2429 - Design a Food Rating System
# Date: 2023-12-17
# Runtime: 758 ms, Memory: 47.3 MB
# Submission Id: 1121611644


from collections import defaultdict

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisines = defaultdict(list)
        self.food_data = {}
        
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_data[food] = (cuisine, rating)
            heapq.heappush(self.cuisines[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, rating = self.food_data[food]
        self.food_data[food] = cuisine, newRating
        heapq.heappush(self.cuisines[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        cuisines = self.cuisines[cuisine]
        while True:
            rating, food = cuisines[0]
            if self.food_data[food][1] != -rating:
                heapq.heappop(cuisines)
            else:
                break
        return cuisines[0][1]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)