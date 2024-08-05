#include <stdio.h>
#include <limits.h>
#define V 4
int tsp(int graph[][V], int s) {
    int vertex[V-1];
    for (int i = 0, j = 0; i < V; i++) {
        if (i != s) vertex[j++] = i;
    }

    int min_path = INT_MAX;
    do {
        int current_pathweight = 0;
        int k = s;
        for (int i = 0; i < V - 1; i++) {
            current_pathweight += graph[k][vertex[i]];
            k = vertex[i];
        }
        current_pathweight += graph[k][s];
        min_path = min(min_path, current_pathweight);
    } while (next_permutation(vertex, vertex + V - 1));

    return min_path;
}

int main() {
    int graph1[V][V] = {{0, 10, 15, 20},
                       {10, 0, 35, 25},
                       {15, 35, 0, 30},
                       {20, 25, 30, 0}};
    printf("Output: %d\n", tsp(graph1, 0));  // Output: 80

    int graph2[V][V] = {{0, 10, 10, 10},
                       {10, 0, 10, 10},
                       {10, 10, 0, 10},
                       {10, 10, 10, 0}};
    printf("Output: %d\n", tsp(graph2, 0));  // Output: 40

    int graph3[V][V] = {{0, 1, 2, 3},
                       {1, 0, 4, 5},
                       {2, 4, 0, 6},
                       {3, 5, 6, 0}};
    printf("Output: %d\n", tsp(graph3, 0));  // Output: 12

    return 0;
}
