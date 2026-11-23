# Multi-Agent Autonomous Drone Simulation

## 1. General Objective

The objective of this project is to design, implement, and evaluate a 2D grid-based simulation for autonomous multi-agent navigation. Multiple drone agents must navigate from their designated starting coordinates to their target destinations while avoiding static obstacles and dynamically coordinating with one another to prevent collisions.

Specifically, the project aims to:
* Model a discrete 2D grid environment with configurable static obstacles.
* Compute optimal obstacle-free paths for individual agents using the A* pathfinding algorithm.
* Implement a reactive coordination mechanism that detects potential collisions and resolves them through priority-based yielding.
* Evaluate system performance across different traffic densities (e.g., 2-agent vs. 5-agent scenarios).

---

## 2. Project Structure

The codebase follows a clean, modular Python script layout where each core responsibility is isolated into its own file:

```text
src/
├── environment.py   # 2D grid representation, boundaries, and obstacle management
├── agent.py         # Drone state, coordinates, and movement updates
├── pathfinder.py    # A* pathfinding wrapper using the third-party 'pathfinding' library
├── simulation.py    # Movement engine, conflict resolution, and metrics logging
└── run.py           # Experiment runner configuring obstacle maps and multi-agent scenarios
```

---

## 3. System Mechanism

The simulation operates through a **Reactive Loop with Priority-Based Yielding**. Instead of computing complex time-space trajectories upfront, agents plan independently and resolve traffic conflicts dynamically as they occur.

### Step-by-Step Workflow

1. **Initialization & Path Planning:**
   * The `Environment` is constructed with the specified dimensions and static obstacles.
   * Each `Agent` is reset to its `start_position` with status `ACTIVE`, and `find_path_a_star()` calculates its shortest path around static obstacles.
   * A progress dictionary (`path_indices`) initializes a cursor at index `0` for every agent to track its current step along its path list.

2. **Discrete Time-Step Loop:**
   * The simulation advances tick-by-tick up to a safety limit (`max_steps`) to prevent infinite loops in case of deadlocks.
   * At each tick, the simulator records a snapshot of all agents' `current_positions`.

3. **Look-Ahead (Intended Moves):**
   * Every active agent looks one step ahead in its pre-calculated `path` (`idx + 1`) to determine its intended `target_cell` for the current tick.

4. **Conflict Detection & Priority Resolution:**
   * The simulator iterates through active agents and maintains a `claimed_positions` registry for the current tick.
   * A conflict is flagged if an agent's `target_cell` meets either condition:
     * **Occupied (`is_occupied`):** Another agent is currently sitting on that cell.
     * **Contested (`is_contested`):** Another agent has already claimed that cell as its intended move for the current tick.
   * **Priority Tie-Breaker:** Agents with a lower `agent_id` hold higher priority. When a conflict occurs, the lower-priority agent **yields by holding its current position** for one time step, allowing the higher-priority agent to pass safely.

5. **Movement Execution & Termination:**
   * All resolved moves are executed for the current tick. Agents that successfully advance increment their `path_indices` cursor and update their position via `move_to()`.
   * Once all agents reach `agent_status == "REACHED"`, the loop terminates early and outputs the final performance metrics (Total Steps, Total Distance, Average Distance per Agent, Yield Events, Success Rate, and Execution Time).


## 4. Running The Simulation
1. `pip install -r requirements.txt`
2. `python src/run.py`

