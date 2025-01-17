class Rabbit:
    def __init__(self):
        self.food_capacity = 0
        self.max_food_capacity = 45
        self.metabolism = 3
        self.reproduction_age = 10
        self.prob_reproduction = 0.5
        self.min_food_reproduct = 40
        self.max_age = 25
        self.rabbit_value = 10
        self.die_cooldown = 3
        self.age = 1

class Wolf:
    def __init__(self):
        self.food_capacity = 0
        self.max_food_capacity = 200
        self.metabolism = 2
        self.reproduction_age = 10
        self.prob_reproduction = 0.5
        self.min_food_reproduct = 120
        self.max_age = 50
        self.die_cooldown = 2
        self.age = 1

class Grass:
    def __init__(self):
        self.growth_rate = 5
        self.grass_value = 10