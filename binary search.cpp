#include <stdio.h>
int binarySearch(int arr[], int l, int h) 
{
    int left = 0, right = l - 1;
    while (left <= right) 
	{
        int mid = left + (right - left) / 2;
        if (arr[mid] == h) 
		{
            return mid;
        }
        if (arr[mid] < h) 
		{
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}
int main() 
{
    int arr[] = {2, 3, 4, 10, 40};
    int l = sizeof(arr) / sizeof(arr[0]);
    int h = 10;
    int result = binarySearch(arr, l, h);
    if (result != -1) {
        printf("Element is present at index %d\n", result);
    } 
	else 
	{
        printf("Element is not present in array\n");
    }
    return 0;
}

