#include <stdio.h>
#include <stdlib.h>

int main()
{   int k;
    int i;
    while(1){
    i=2;
    scanf("%d",&k);
    while(i<=k){
           if(k%i==0){
            break;
           }
           i++;

    }
    if(i<k){
    printf("%d²»ÊÇËØÊý\n",k);

    return 0;
}
