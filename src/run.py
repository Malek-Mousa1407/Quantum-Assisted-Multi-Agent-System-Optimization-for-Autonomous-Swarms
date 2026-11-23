from simulation import run_agent_simulation
from agent import Agent
import random


def get_obstacles():
     obstacles = [
        (1, 1), (3, 2), (7, 1), (8, 3),
        (1, 4), (3, 4), (7, 4), (8, 6),
        (1, 7), (3, 8), (6, 8), (8, 8),
        (2, 9), (4, 2), (7, 9), (9, 2),
        (4,3),  (4, 4), (1,8) , (3, 3)
    ]
     
     k = random.randint(1, len(obstacles))
     return random.sample(obstacles, k)


def get_agents():
    return [
        Agent(agent_id=1, start_position=(1, 5), target_posistion=(8, 5)),
        Agent(agent_id=2, start_position=(5, 1), target_posistion=(5, 8)),
        Agent(agent_id=3, start_position=(2, 4), target_posistion=(2, 8)),
        Agent(agent_id=4, start_position=(3, 3), target_posistion=(7, 3)),
        Agent(agent_id=5, start_position=(6, 0), target_posistion=(6, 7)),
    ]


for i in range(3):
    run_agent_simulation(get_agents()[:2], get_obstacles())
    print("\n"*8)
    run_agent_simulation(get_agents(), get_obstacles())