import argparse
import numpy as np 
from animal import Rabbit, Wolf, Glass
from state import State

def simulate(turns):
    rabbits = [Rabbit() for _ in range(state_info.n_rabbit)]
    wolves = [Wolf(metabolism=20) for _ in range(state_info.n_wolf)]  # กูลองเพิ่ม metabolism rate เป็น 5, 10, 20 ดู เพราะว่าถ้าเป็น default หมามันจะตายยากมาก 
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

                if rabbit.age % rabbit.reproduction_age == 0 and rabbit.food_capacity > rabbit.min_food_reproduct and np.random.rand() > rabbit.prob_repoduction:
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_turns", type=int, default=50, help="number of turn")
    parser.add_argument("--n_grass", type=int, default=400, help="number of grass box")
    parser.add_argument("--n_rabbit", type=int, default=20, help="number of rabbit")
    parser.add_argument("--n_wolf", type=int, default=2, help="number of wolf")
    opt = parser.parse_args()
    print("n_grass", opt.n_grass)
    state_info = State(opt.n_grass, opt.n_rabbit, opt.n_wolf)
    simulate(opt.n_turns)