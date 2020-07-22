"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create a plan_to_visit queue and add starting_vertex to it
        plan_to_visit = Queue()
        plan_to_visit.enqueue(starting_vertex)
        # create a Set for visited_vertices
        visited_vertices = set()
        # while the plan_to_visit queue is not empty:
        while plan_to_visit.size() > 0:
            # dequeue the first vertex on the queue
            current_vertex = plan_to_visit.dequeue()
            # if its not been visited
            if current_vertex not in visited_vertices:
                # print the vertex
                print(current_vertex)
                # mark it as visited, (add it to visited_vertices)
                visited_vertices.add(current_vertex)
                # add all neighbors to the queue
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:
                        plan_to_visit.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a plan_to_visit stack and add starting_vertex to it
        plan_to_visit = Stack()
        plan_to_visit.push(starting_vertex)
        # create a Set for visited_vertices
        visited_vertices = set()
        # while the plan_to_visit stack is not empty:
        while plan_to_visit.size() > 0:
            # pop the first vertex on the queue
            current_vertex = plan_to_visit.pop()
            # if its not been visited
            if current_vertex not in visited_vertices:
                # print the vertex
                print(current_vertex)
                # mark it as visited, (add it to visited_vertices)
                visited_vertices.add(current_vertex)
                # add all neighbors to the stack
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:
                        plan_to_visit.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # create a Set for visited_vertices
        # while the plan_to_visit stack is not empty:
            # pop the first vertex on the stack
            # if its not been visited
                # print the vertex
                # mark it as visited, (add it to visited_vertices)
                # add all neighbors to the stack

        if visited is None:
            visited = set()

        current = starting_vertex
        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)
            for neighbor in self.get_neighbors(current):
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create an empty queue, and enqueue a PATH to the starting vertex
        paths_to_check = Queue()
        # queue.enqueue([starting_vertex])
        paths_to_check.enqueue([starting_vertex])
        # create a set for visited vertices
        visited_vertices = set()
        # while the queue is not empty
        while paths_to_check.size() > 0:
    #     dequeue the first PATH
            current_path = paths_to_check.dequeue()
    #     grab the last vertex in the path
            end = current_path[-1]
    #     if it hasn't been visited
            if end not in visited_vertices:
    #         check if it's the target
                if end == destination_vertex:
    #             return the path
                    return current_path
    #         mark it as visited
                visited_vertices.add(end)
    #         make new versions of the current path, with each neighbor added to it
                for neighbor in self.vertices[end]:
    #             duplicate the path
                    new_path = current_path.copy()
    #             add the neighbor
                    new_path.append(neighbor)
    #             add the new path to the queue
                    paths_to_check.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Artem's enquing a tuple approach:
        # neighbors_to_visit = Stack()
        # visited_vertices = set()
        # neighbors_to_visit.push((starting_vertex, []))
        # while neighbors_to_visit.size() > 0:
        #     current_vertex_plus_path = neighbors_to_visit.pop()
        #     current_vertex = current_vertex_plus_path[0]
        #     if current_vertex not in visited_vertices:
        #         if current_vertex == destination_vertex:
        #             updated_path = current_vertex_plus_path[1] + [current_vertex]
        #             return updated_path
        #         visited_vertices.add(current_vertex)
        #         for neighbor in self.get_neighbors(current_vertex):
        #             updated_path = current_vertex_plus_path[1] + [current_vertex]
        #             neighbors_to_visit.push((neighbor, updated_path))
        # create a stack for paths to check
        paths_to_check = Stack()
        # push the starting_vertex onto the stack
        paths_to_check.push([starting_vertex])
        # create a set for visited vertices
        visited_vertices = set()
        # add node to visited
        visited_vertices.add(starting_vertex)
        # while stack isn't empty:
        while paths_to_check.size() > 0:
    #         pop off the stack
            path = paths_to_check.pop()
    #         check last element in path:
            if path[-1] == destination_vertex:
    #             return path
                return path
    #         for neighbor in neghbors:
            for neighbor in self.get_neighbors(path[-1]):
    #             if not in visited:
                if neighbor not in visited_vertices:
    #                 add to visited
                    visited_vertices.add(neighbor)
    #                 push new path onto stack:
    #                     copy path
                    new_path = path.copy()
    #                     add neighbor
                    new_path.append(neighbor)
    #                     push path
                    paths_to_check.push(new_path)


    def dfs_recursive(self, starting_vertex, destination_vertex, path=None, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        if path is None:
            path = [starting_vertex]
        print("PATH", path)
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        if path[-1] == destination_vertex:
            print("HERE!!!")
            return path
        for neighbor in self.get_neighbors(path[-1]):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path.copy()
                new_path.append(neighbor)
                # path = new_path
                self.dfs_recursive(neighbor, destination_vertex, new_path, visited)
                # return path
        # return path

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)
    print("BFT")
    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("DFT")
    graph.dft(1)
    graph.dft_recursive(1)
    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))

import re
class Thing:
    def __init__(self, name, verification_format, decryption_key=None, method=None):
        self.name = name
        self.verification_format = re.compile(verification_format)
        self.decryption_key = decryption_key
        self.method = method

    def verify(self, contact_id):
        if re.match(self.verification_format, contact_id):
            return True
        else:
            return False


ver = "[a-z]{4}[0-9]{5,8}"

thing = Thing("Hi", ver, decrypt_key="123456789", method="Hello")
print(thing.name)
print(thing.verify("help12345"))
print(thing.method)
