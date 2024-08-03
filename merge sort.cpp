#include <stdio.h>

void combine(int a[], int low, int mid, int high) {
    int temp[high - low + 1];
    int i = low, j = mid + 1, k = 0;

    while (i <= mid && j <= high) {
        if (a[i] <= a[j]) {
            temp[k] = a[i];
            i++;
        } else {
            temp[k] = a[j];
            j++;
        }
        k++;
    }

    while (i <= mid) {
        temp[k] = a[i];
        i++;
        k++;
    }

    while (j <= high) {
        temp[k] = a[j];
        j++;
        k++;
    }

    for (i = low, k = 0; i <= high; i++, k++) {
        a[i] = temp[k];
    }
}

void mergesort(int a[], int low, int high) {
    if (low < high) {
        int mid = (low + high) / 2;
        mergesort(a, low, mid);
        mergesort(a, mid + 1, high);
        combine(a, low, mid, high);
    }
}

int main() {
    int a[] = {2, 5, 6, 9, 1, 0, 4, 3};
    int n = sizeof(a) / sizeof(a[0]);
    int i;

    mergesort(a, 0, n - 1);

    for (i = 0; i < n; i++) {
        printf("%d\t", a[i]);
    }
    printf("\n");

    return 0;
}
