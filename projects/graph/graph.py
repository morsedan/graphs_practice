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
        if v1 not in self.vertices or v2 not in self.vertices:
            raise ValueError("vertex does not exist")
            return  # raise exception?

        self.vertices[v1].add(v2)


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise ValueError("vertex does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """



        q = Queue()
        visited = set()

        q.enqueue(starting_vertex)
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                print(v)
                visited.add(v)
                for edge in self.vertices[v]:
                    q.enqueue(edge)


            # for edge in self.vertices[vertex]:
            #     if edge not in v:
            #         q.enqueue(edge)
            #
            # print(vertex)
            # v.add(vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        # Not sure what this is... looks like bfs, but doesn't return anything.
        # q = Queue()
        # q.enqueue([starting_vertex])
        # visited = set()
        # while q.size() > 0:
        #     path = q.dequeue()
        #     if path[-1] not in visited:
        #         # print(path[-1])
        #         visited.add(path[-1])
        #         for next_vert in self.get_neighbors(path[-1]):
        #             new_path = list(path)
        #             new_path.append(next_vert)
        #             q.enqueue(new_path)

        s = Stack()
        v = set()

        s.push(starting_vertex)

        while s.size() > 0:
            vertex = s.pop()
            if vertex not in v:
                print(vertex)
                v.add(vertex)
                for edge in self.vertices[vertex]:
                    s.push(edge)


            # for edge in self.vertices[vertex]:
            #     if edge not in v:
            #         s.push(edge)
            #         v.add(edge)
            #
            # v.add(vertex)
            # print(vertex)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)


        # visited.add(starting_vertex)
        # print(starting_vertex)
        # for neighbor in self.vertices[starting_vertex]:
        #     if neighbor not in visited:
        #         visited.add(neighbor)
        #         self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        visited = set()
        path = [starting_vertex]
        q.enqueue(path)
        while q.size() > 0:
            check = q.dequeue()
            end = check[-1]
            if end == destination_vertex:
                return check
            if end not in visited:
                visited.add(end)
                for neighbor in self.vertices[end]:
                    q.enqueue(check + [neighbor])
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        visited = set()
        path = [starting_vertex]

        s.push(path)

        while s.size() > 0:
            check = s.pop()
            end = check[-1]
            if end == destination_vertex:
                return check
            if end not in visited:
                visited.add(end)
                for neighbor in self.vertices[end]:
                    s.push(check + [neighbor])
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        # print(starting_vertex == destination_vertex)
        # print(path, starting_vertex, visited)
        path.append(starting_vertex)
        visited.add(starting_vertex)
        for neighbor in self.vertices[starting_vertex]:
            # print(neighbor, neighbor in visited)
            if neighbor not in visited:
                # print(neighbor, destination_vertex, visited, path)
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path.copy())
                if new_path[-1] == destination_vertex:
                    return new_path
        # else:
        #     path.append(starting_vertex)
        #     return path
        return path
"""
add start to path
add start to visited
for neighbor:
    if neighbor not visited:
    path = recurse with neighbor
    if last is destination:
        return new_path
return the path


path = [1, 2, 4, 6]
visited = {1, 2, 4, 6}

"""



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
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    graph.dft_recursive(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
