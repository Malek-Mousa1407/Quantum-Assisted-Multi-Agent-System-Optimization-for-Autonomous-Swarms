# Quantum Computing Extension

## Defining Quantum Optimization and QUBO

- Quantum optimization is an approach that uses quantum computing techniques to search for optimal or good solutions to problems involving many possible choices.

- Quantum Annealing and QAOA (Quantum Approximate Optimization Algorithm) are examples of quantum optimization methods.

- QUBO stands for Quadratic Unconstrained Binary Optimization. It is a mathematical formulation that represents an optimization problem using binary variables (0 and 1).

## 1. Which part of the problem could benefit from quantum optimization?

Quantum optimization could improve the decision-making process when multiple drones compete for the same cell or when their planned movements interfere with one another.

In our project, A* would continue calculating individual paths, while QUBO could coordinate the movement decisions of all active drones.

## 2. How could the problem be represented using Quadratic Unconstrained Binary Optimization?

For each drone, we define binary variables representing its possible actions.

For example:

$$
x_{i,a}=
\begin{cases}
1 & \text{Drone }i\text{ selects action }a\\
0 & \text{Otherwise}
\end{cases}
$$

The possible actions could include:

- Moving to the next cell in its A* path.
- Waiting for one time step.
- Taking an alternative movement, if available.

We introduce penalties to prevent conflicting movements:

$$
P_{\text{collision}}=B x_{1,A}x_{2,A}
$$

Where B is a large penalty value. If both drones choose cell A during the same time step, the penalty is applied.

Combine the different costs and penalties into one QUBO function:

$$
\boxed{
E=
C_{\text{movement}}
+
P_{\text{selection}}
+
P_{\text{collision}}
+
P_{\text{other conflicts}}
}
$$

The objective is:

$$
\min E
$$

The optimizer attempts to find a combination of drone movements that:

1. Allows every drone to select a valid action.
2. Prevents collisions.
3. Minimizes unnecessary waiting.
4. Reduces unnecessary movement.
5. Improves the overall performance of the group.

## 3. What advantages and limitations might a quantum-assisted approach have compared with classical algorithms?

### Advantages
- Better group coordination.
- Potential reduction in waiting time.
- Ability to optimize multiple objectives simultaneously.

### Limitations
- Quantum hardware requirements.
- Model complexity.
- Penalty values must be selected carefully.
- No guaranteed advantage over classical algorithms.