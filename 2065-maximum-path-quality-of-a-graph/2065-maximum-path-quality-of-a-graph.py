class Solution:

    def __init__(self):
        self.maximum_path_quality = 0

    def depth_first_search(self, current_cost, current_time_taken, maximum_time, current_node, pair_nodes_time_map, values_list, adjacency_list, visited_set):
        if current_time_taken > maximum_time:
            return

        if current_node == 0:
            self.maximum_path_quality = max(self.maximum_path_quality, current_cost)

        visited_set.add(current_node)

        for neighbour_node in adjacency_list.get(current_node, []):
            new_time_taken = current_time_taken + pair_nodes_time_map[(current_node, neighbour_node)]
            new_cost = current_cost + values_list[neighbour_node] if neighbour_node not in visited_set else current_cost
            self.depth_first_search(new_cost, new_time_taken, maximum_time, neighbour_node, pair_nodes_time_map, values_list, adjacency_list, visited_set.copy())

    def maximalPathQuality(self, values_list, edges_details_list, maximum_time):
        adjacency_list = {}
        pair_nodes_time_map = {}

        for node_1, node_2, time in edges_details_list:
            adjacency_list.setdefault(node_1, []).append(node_2)
            adjacency_list.setdefault(node_2, []).append(node_1)
            pair_nodes_time_map[(node_1, node_2)] = time
            pair_nodes_time_map[(node_2, node_1)] = time

        self.depth_first_search(values_list[0], 0, maximum_time, 0, pair_nodes_time_map, values_list, adjacency_list, set())

        return self.maximum_path_quality
