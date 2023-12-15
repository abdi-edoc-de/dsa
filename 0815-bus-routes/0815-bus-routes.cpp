
class Solution {
public:
    int numBusesToDestination(std::vector<std::vector<int>>& routes, int source, int target) {
        if (source == target) return 0;

        // Create a map to store the buses that cover each bus stop
        std::unordered_map<int, std::unordered_set<int>> stopToBuses;
        for (int i = 0; i < routes.size(); ++i) {
            for (int stop : routes[i]) {
                stopToBuses[stop].insert(i);
            }
        }

        // BFS queue
        std::queue<int> q;
        // Set to track visited bus stops
        std::unordered_set<int> visitedStops;
        // Set to track visited buses
        std::unordered_set<int> visitedBuses;

        q.push(source);
        visitedStops.insert(source);
        int buses = 0;

        while (!q.empty()) {
            int size = q.size();
            ++buses;

            for (int i = 0; i < size; ++i) {
                int currStop = q.front();
                q.pop();

                for (int bus : stopToBuses[currStop]) {
                    if (visitedBuses.count(bus)) continue;

                    visitedBuses.insert(bus);

                    for (int nextStop : routes[bus]) {
                        if (visitedStops.count(nextStop)) continue;

                        if (nextStop == target) {
                            return buses;
                        }

                        visitedStops.insert(nextStop);
                        q.push(nextStop);
                    }
                }
            }
        }

        return -1; // Not possible to reach the target
    }
};
