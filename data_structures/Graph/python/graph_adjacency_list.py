"""
Graph Implementation using Adjacency List in Python

Description:
This module defines a Graph data structure using an adjacency list.
It supports adding vertices, adding directed/undirected edges, and printing the graph.

Time Complexity:
- add_vertex: O(1)
- add_edge: O(1)
- print_graph: O(V + E) where V is the number of vertices and E is the number of edges.

Space Complexity: O(V + E) for storing the graph.
"""

class Graph:
    """Graph represented using an adjacency list."""

    def __init__(self):
        # Initialize an empty dictionary to store adjacency lists
        self.graph = {}

    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph if it doesn’t already exist.
        :param vertex: The vertex label (e.g., 'A', 'B', 1, etc.)
        """
        if vertex not in self.graph:
            self.graph[vertex] = []
        else:
            print(f"Vertex '{vertex}' already exists!")

    def add_edge(self, vertex1, vertex2, directed=False):
        """
        Adds an edge between two vertices.
        :param vertex1: The starting vertex.
        :param vertex2: The ending vertex.
        :param directed: If False, creates an undirected edge (default).
        """
        # Add missing vertices automatically
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)

        # Add the edge from vertex1 to vertex2
        self.graph[vertex1].append(vertex2)

        # If undirected, also add the reverse connection
        if not directed:
            self.graph[vertex2].append(vertex1)

    def print_graph(self):
        """Prints the adjacency list of the graph."""
        print("Graph Adjacency List:")
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")

# -------------------------------------------------------------
# Example usage (runnable block)
# -------------------------------------------------------------
if __name__ == "__main__":
    # Create a new graph instance
    g = Graph()

    # Add vertices
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('C')

    # Add edges
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'C', directed=True)

    # Print the adjacency list
    g.print_graph()
