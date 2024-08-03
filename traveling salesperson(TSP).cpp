#include <stdio.h>
#include <limits.h>
#define N 4  
int dist[N][N] = {
    {0, 10, 15, 20},
    {5, 0, 9, 10},
    {6, 13, 0, 12},
    {8, 8, 9, 0}
};
int memo[N][1 << N];
void initMemo() {
    for (int i = 0; i < N; ++i) 
	{
        for (int j = 0; j < (1 << N); ++j) 
		{
            memo[i][j] = -1;
        }
    }
}
int tsp(int pos, int mask) 
{
    if (mask == (1 << N) - 1) 
	{
        return dist[pos][0]; 
    }
    if (memo[pos][mask] != -1) 
	{
        return memo[pos][mask];
    }
    int res = INT_MAX;
    for (int city = 0; city < N; ++city) 
	{
        if ((mask & (1 << city)) == 0) 
		{ 
            int newCost = dist[pos][city] + tsp(city, mask | (1 << city));
            if (newCost < res) 
			{
                res = newCost;
            }
        }
    }
    memo[pos][mask] = res; 
    return res;
}
int main() 
{
    initMemo();
    int result = tsp(0, 1); 
    printf("The cost of the most efficient tour = %d\n", result);
    return 0;
}

