import time
from environment import Environment
from agent import Agent
from pathfinder import find_path_a_star

def run_agent_simulation(agents, obstacles):
    start_time = time.perf_counter()
    print("--- Starting Drone Simulation ---")
    
    env = Environment(width=10, height=10, obstacles=obstacles)
    print(f"Environment created: 10x10 with {len(env.obstacles)} obstacle cells.")

    for agent in agents:
        agent.path = find_path_a_star(env, agent.start_position, agent.target_posistion)
        print(f"Spawned: {agent} | Path: {agent.path}")

    path_indices = {agent.agent_id: 0 for agent in agents}

    max_steps = 40
    step_count = 0
    total_yields = 0
    total_distance = 0

    while step_count < max_steps:
        step_count += 1
        print(f"\n Time Step {step_count} ")
        
        current_positions = {agent.agent_id: agent.current_posistion for agent in agents}

        intended_moves = {}
        for agent in agents:
            if agent.agent_status == "REACHED":
                continue
                
            idx = path_indices[agent.agent_id]
            if idx + 1 < len(agent.path):
                intended_moves[agent.agent_id] = agent.path[idx + 1]


        claimed_positions = {}
        for agent in agents:
            if agent.agent_status == "REACHED":
                continue
            
            target_cell = intended_moves[agent.agent_id]
            
            is_occupied = (target_cell in current_positions.values() and target_cell != agent.current_posistion)
            is_contested = target_cell in claimed_positions.values()

            if (is_occupied or is_contested) and target_cell != agent.current_posistion:
                conflicting_agent_id = next((aid for aid, pos in claimed_positions.items() if pos == target_cell), None)
                
                if conflicting_agent_id and conflicting_agent_id < agent.agent_id:
                    print(f"Conflict! Agent {agent.agent_id} yields to Agent {conflicting_agent_id} and holds at {agent.current_posistion}")
                    intended_moves[agent.agent_id] = agent.current_posistion
                    claimed_positions[agent.agent_id] = agent.current_posistion
                    total_yields += 1
                elif not conflicting_agent_id:
                    print(f"Conflict! Agent {agent.agent_id} yields and holds position at {agent.current_posistion}")
                    intended_moves[agent.agent_id] = agent.current_posistion
                    claimed_positions[agent.agent_id] = agent.current_posistion
                    total_yields += 1
                else:
                    claimed_positions[agent.agent_id] = target_cell
            else:
                claimed_positions[agent.agent_id] = target_cell

        for agent in agents:
            if agent.agent_status == "REACHED":
                continue

            next_position = intended_moves[agent.agent_id]
            
            if next_position != agent.current_posistion:
                path_indices[agent.agent_id] += 1
                total_distance += 1
                
            agent.move_to(next_position)
            print(f"Agent {agent.agent_id} -> moved to {agent.current_posistion} [status: {agent.agent_status}]")


        if all(agent.agent_status == "REACHED" for agent in agents):
            print("\nSuccess: All drones have reached their destinations!")
            break

    exec_time_ms = (time.perf_counter() - start_time) * 1000
    reached_count = sum(1 for a in agents if a.agent_status == "REACHED")

    metrics = {
        "Scenario": f"{len(agents)} Agents",
        "Total Steps": step_count,
        "Total Distance": total_distance,
        "Collision Events": total_yields,
        "Success Rate": round((reached_count / len(agents)) * 100, 1),
        "Execution Time": round(exec_time_ms, 2)
    }

    print("\n--- Simulation Finished ---")
    
    for agent in agents:
        print(agent)
    print(f"Metrics: {metrics}")


    print("\n"*3)
    return metrics