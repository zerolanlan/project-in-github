#include <stdio.h>
#include <stdlib.h>

int main()
{   int i;
    for(i=1;i<=10;i++)
    {
        if(i==6)
            break;
        printf("%4d",i);
    }
    printf("game over!\n");
    return 0;
}
