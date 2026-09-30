# algo_runner

A Flask REST API that runs graph algorithms on a graph sent as JSON and returns the result together with step-by-step execution data.

Currently implemented: **Dijkstra's shortest path algorithm**.
This is the backend for AlgoDemic, a separate project (an interactive graph-drawing board) that sends requests to this API.

## How it works

The client sends a graph as JSON under the `"graph"` key. The server validates the input (including a negative-weight check), runs the chosen algorithm, and returns:

- the distance to each node
- the previous node (predecessor) on the shortest path to each node
- the execution steps of the algorithm

Undirected graphs are sent with every edge in both directions.

## Run server

```bash
python backend/server.py 
```
