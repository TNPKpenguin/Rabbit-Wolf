import numpy as np 
from animal import Rabbit, Wolf, Glass
from state import State

state_info = State()

def simulate(turns):
    rabbits = [Rabbit() for _ in range(state_info.n_rabbit)]
    wolves = [Wolf() for _ in range(state_info.n_wolf)]
    grass_blocks = state_info.n_grass
    grass = Glass()

    for turn in range(turns):
        print(f"Step {turn+1}/{turns}")

        grass_blocks = min(grass_blocks + grass.growth_rate, grass.growth_rate * 80)

        for rabbit in rabbits:
            if grass_blocks > 0:
                rabbit.food_capacity = min(rabbit.food_capacity + grass.grass_value, 45)
                grass_blocks -= 1

                rabbit.food_capacity -= rabbit.metabolism
                rabbit.age += 1

                if rabbit.age > rabbit.reproduction_age and rabbit.food_capacity > rabbit.min_food_reproduct and np.random.rand() < rabbit.prob_reproduct:
                    rabbits.append(Rabbit())
        
        for wolf in wolves:
            if rabbits:
                prey = np.random.choice(rabbits)
                wolf.food_capacity = min(wolf.food_capacity + prey.rabbit_value, 200)
                rabbits.remove(prey)
            
            wolf.food_capacity -= wolf.metabolism
            wolf.age += 1

            if wolf.food_capacity <=0 or wolf.age >= wolf.max_age:
                print("die")
                wolves.remove(wolf)
            
            if wolf.age % wolf.reproduction_age == 0 and wolf.food_capacity > wolf.min_food_reproduct and np.random.rand() > wolf.prob_repoduction:
                wolves.append(Wolf())
        
        print(f"Grass: {grass_blocks}, Rabbits: {len(rabbits)}, Wolves: {len(wolves)}")
        
        if not rabbits and not wolves:
            print("Simulation ended: All animals have died.")
            break

simulate(200)