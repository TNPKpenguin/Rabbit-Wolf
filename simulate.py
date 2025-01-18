import argparse
import numpy as np 
import matplotlib.pyplot as plt
from animal import Rabbit, Wolf, Grass
from state import State

def make_graph(grass, rabbits, wolves):
    plt.plot(grass, color="g", label="Grass")
    plt.plot(rabbits, color="b", label="Rabbits")
    plt.plot(wolves, color="r", label="Wolves")
    plt.legend()
    plt.show()

def simulate(turns, is_stop, is_show_graph):
    n_grass, n_rabbits, n_wolves = [], [], []

    rabbits = [Rabbit() for _ in range(state_info.n_rabbit)]
    wolves = [Wolf() for _ in range(state_info.n_wolf)]  
    grass_blocks = state_info.n_grass
    grass = Grass()

    for turn in range(turns):
        print(f"Step {turn+1}/{turns}", end="   ")

        #cal grass_blocks = if turns%5==0 then grass_block growth
        #every turn grass_block growth 5 field but grass_block can't more n_grass
        grass_blocks = min(grass_blocks + grass.growth_rate, state_info.n_grass)

        # Rabbits section
        for rabbit in rabbits:
            if grass_blocks > 0:
                #if food_capacity is 40 but grass_value get 10 but fact not gift point food to 45
                rabbit.food_capacity = min(rabbit.food_capacity + grass.grass_value, rabbit.max_food_capacity)
                grass_blocks -= 1

                rabbit.food_capacity -= rabbit.metabolism
                rabbit.age += 1

                if rabbit.age >= rabbit.reproduction_age and rabbit.food_capacity > rabbit.min_food_reproduct and np.random.rand() > rabbit.prob_reproduction:
                    rabbits.append(Rabbit())

                if rabbit.food_capacity <= 0:
                    rabbit.die_cooldown -= 1
                    if rabbit.die_cooldown == 0:
                        rabbits.remove(rabbit)
                else:
                    rabbit.die_cooldown = 3

                if rabbit.age >= rabbit.max_age:
                    rabbits.remove(rabbit)

        # Wolves section
        #what's the [:]
        for wolf in wolves[:]:
            if rabbits:
                prey = np.random.choice(rabbits)
                
                if np.random.rand() > 0.3:   # if random value > 0.5 = the rabbit was eaten by a wolf
                    wolf.food_capacity = min(wolf.food_capacity + prey.rabbit_value, wolf.max_food_capacity)
                    rabbits.remove(prey)
            
            wolf.food_capacity -= wolf.metabolism
            wolf.age += 1

            if wolf.food_capacity <=0:
                wolf.die_cooldown -= 1
                if wolf.die_cooldown <= 0:
                    wolves.remove(wolf)
            else:
                wolf.die_cooldown = 2
            
            if wolf.age >= wolf.max_age:
                wolves.remove(wolf)

            if wolf.age >= wolf.reproduction_age and wolf.food_capacity > wolf.min_food_reproduct and np.random.rand() > wolf.prob_reproduction:
                wolves.append(Wolf())

        print(f"Grass: {grass_blocks}, Rabbits: {len(rabbits)}, Wolves: {len(wolves)}")
        
        n_grass.append(grass_blocks)
        n_rabbits.append(len(rabbits))
        n_wolves.append(len(wolves))
        

        #if is_stop and not rabbits and not wolves:
        if not rabbits and not wolves:
            print("Simulation ended: All animals have died.")
            break
    if not is_show_graph:
        make_graph(n_grass, n_rabbits, n_wolves)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_turns", type=int, default=60, help="number of turn")
    parser.add_argument("--n_grass", type=int, default=400, help="number of grass box")
    parser.add_argument("--n_rabbit", type=int, default=20, help="number of rabbit")
    parser.add_argument("--n_wolf", type=int, default=2, help="number of wolf")
    parser.add_argument("--no_show_graph", action="store_true", help="if you don't want to show graph")
    parser.add_argument("--stop", action="store_true", help="Stop the simulation when all animals die")
    opt = parser.parse_args()

    state_info = State(opt.n_grass, opt.n_rabbit, opt.n_wolf)
    simulate(opt.n_turns, opt.stop, opt.no_show_graph)
    