class Rabbit:
    def __init__(self, food_capacity=45, metabolism=3, reproduction_age=10, prob_reproduct=0.5, min_food_reproduct=40, max_age=25, rabbit_value=10, die_cooldown=3):
        self.food_capacity = food_capacity
        self.metabolism = metabolism
        self.reproduction_age = reproduction_age
        self.prob_repoduction = prob_reproduct
        self.min_food_reproduct = min_food_reproduct
        self.max_age = max_age
        self.rabbit_value = rabbit_value
        self.die_cooldown = die_cooldown

class Wolf:
    def __init__(self, food_capacity=200, metabolism=2, reproduction_age=10, prob_reproduct=0.5, min_food_reproduct=120, max_age=50, die_cooldown=2):
        self.food_capacity = food_capacity
        self.metabolism = metabolism
        self.reproduction_age = reproduction_age
        self.prob_repoduction = prob_reproduct
        self.min_food_reproduct = min_food_reproduct
        self.max_age = max_age
        self.die_cooldown = die_cooldown

class Glass:
    def __init__(self, growth_rate=5, grass_value=10):
        self.growth_rate = growth_rate
        self.grass_value = grass_value