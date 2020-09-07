#include <stdio.h>
#include <stdlib.h>

int main()
    {
    float sum=0;
    float i;
    int n=1;
    for(i=1;i<=100;i++)
    {
        sum=sum+n/i;
        n*=-1;
    }
    printf("和为%f\n",sum);
    return 0;
}

