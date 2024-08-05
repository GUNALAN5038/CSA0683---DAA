#include <stdio.h>
#include <stdlib.h>

typedef struct Job {
    char id;
    int deadline;
    int profit;
} Job;

int compare(const void *a, const void *b) {
    Job *jobA = (Job *)a;
    Job *jobB = (Job *)b;
    return (jobB->profit - jobA->profit);
}

void jobSequencing(Job jobs[], int n) {
    qsort(jobs, n, sizeof(Job), compare);

    int result[n];
    int slot[n];

    for (int i = 0; i < n; i++) {
        slot[i] = 0;
    }

    for (int i = 0; i < n; i++) {
        for (int j = (jobs[i].deadline < n ? jobs[i].deadline : n) - 1; j >= 0; j--) {
            if (slot[j] == 0) {
                result[j] = i;
                slot[j] = 1;
                break;
            }
        }
    }

    printf("Following is the maximum profit sequence of jobs:\n");
    for (int i = 0; i < n; i++) {
        if (slot[i]) {
            printf("%c ", jobs[result[i]].id);
        }
    }
    printf("\n");
}

int main() {
    Job jobs[] = {
        {'a', 2, 100},
        {'b', 1, 19},
        {'c', 2, 27},
        {'d', 1, 25},
        {'e', 3, 15}
    };
    int n = sizeof(jobs) / sizeof(jobs[0]);

    jobSequencing(jobs, n);

    return 0;
}

