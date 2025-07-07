## Algorithm Implementation Overview

This section gives a quick idea about how these algorithms work in practice.

- **Uninformed searches** explore the problem space without extra knowledge. They try nodes blindly.
- **Informed searches** use heuristics (rules of thumb) to guess which nodes are best to explore.
- **Local searches** improve a single solution step-by-step, good for optimization.
- **Game playing algorithms** decide the best move assuming an opponent also plays optimally.

---

## Uninformed Search Algorithms

### Breadth-First Search (BFS)  
- **How it works:** Explores nodes level by level, starting from the root.  
- **Use cases:** Finding shortest path in maps, social networks.  
- **Complexity:** Time and Space = O(b^d) (b = branching factor, d = depth).

---

### Depth-First Search (DFS)  
- **How it works:** Goes deep down one path until it can't go further, then backtracks.  
- **Use cases:** Puzzle solving, checking connectivity.  
- **Complexity:** Time = O(b^m), Space = O(b*m) (m = max depth).

---

### Iterative Deepening Search (IDS)  
- **How it works:** Runs DFS repeatedly with increasing depth limits.  
- **Use cases:** When depth is unknown, combines DFS and BFS benefits.  
- **Complexity:** Time = O(b^d), Space = O(b*d).

---

### Bidirectional Search  
- **How it works:** Searches forward from start and backward from goal simultaneously.  
- **Use cases:** Fast shortest path finding.  
- **Complexity:** Time and Space = O(b^(d/2)).

---

### Depth-Limited Search (DLS)  
- **How it works:** Like DFS but stops at a set depth limit.  
- **Use cases:** Avoid infinite loops, control search depth.  
- **Complexity:** Time = O(b^l), Space = O(b*l) (l = depth limit).

---

## Informed Search Algorithms

### Heuristic Search  
- **How it works:** Uses a heuristic function to estimate how close to goal a node is.  
- **Use cases:** Route finding, AI problem solving.  
- **Complexity:** Depends on heuristic quality.

---

### Best First Search  
- **How it works:** Always expands the most promising node based on heuristic.  
- **Use cases:** Puzzle solving, pathfinding.  
- **Complexity:** Time & Space up to O(b^m).

---

### A* Search  
- **How it works:** Combines cost so far and estimated cost to goal to pick nodes.  
- **Use cases:** GPS navigation, games.  
- **Complexity:** Time and Space O(b^d), but efficient with good heuristics.

---

### AO* Algorithm  
- **How it works:** Solves AND-OR graphs (problems with subgoals and alternatives).  
- **Use cases:** Task planning, expert systems.  
- **Complexity:** Varies by problem size.

---

## Local Search Algorithms

### Hill Climbing  
- **How it works:** Starts with a solution, moves to a better neighbor until no improvement.  
- **Use cases:** Optimization problems.  
- **Complexity:** Fast but can get stuck at local best solutions.

---

### Beam Search  
- **How it works:** Like BFS but only keeps best few nodes at each level (beam width).  
- **Use cases:** Speech recognition, machine translation.  
- **Complexity:** Time & Space depend on beam width and depth.

---

## Game Playing Algorithms

### Minimax Algorithm  
- **How it works:** Explores moves assuming both players try to win or minimize loss.  
- **Use cases:** Chess, Tic-Tac-Toe.  
- **Complexity:** Time = O(b^m), Space = O(m).

---

### Alpha-Beta Pruning  
- **How it works:** Cuts off branches that won't affect the final decision, speeding Minimax.  
- **Use cases:** Same as Minimax but faster.  
- **Complexity:** Best case Time = O(b^(m/2)).

---
