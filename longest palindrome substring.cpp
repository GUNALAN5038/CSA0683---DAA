#include <stdio.h>
#include <string.h>
void printSubStr(const char* str, int low, int high)
{
	int i;
    for(i = low; i <= high; ++i)
        printf("%c", str[i]);
}
int longestPalSubstr(const char* str)
{
    int i,j,k,n,maxLength,start,flag;
    n = strlen(str);
    maxLength = 1, start = 0;
    for (i = 0; i < n; i++)
    {
        for (j = i; j < n; j++)
        {
            flag = 1;
           for (k = 0; k < (j - i + 1) / 2; k++)
                if (str[i + k] != str[j - k])
                    flag = 0;

            if (flag && (j - i + 1) > maxLength) 
            {
                start = i;
                maxLength = j - i + 1;
            }
        }
    }
    printf("Longest palindrome substring is: ");
    printSubStr(str, start, start + maxLength - 1);
    printf("\n");
    return maxLength;
}
int main()
{
    const char* str = "aaaabbaa";
    printf("Length is: %d\n", longestPalSubstr(str));
    return 0;
}
