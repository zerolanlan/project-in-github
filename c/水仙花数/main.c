#include <stdio.h>
#include <stdlib.h>

int main()
{   int bai,shi,ge;


    for(int i=100;i<=999;i++){
        ge=i%10;
        shi=i/10%10;
        bai=i/100%10;
        if((bai*bai*bai+shi*shi*shi+ge*ge*ge)==i){
            printf("%dÊÇË®ÏÉ»¨ËØ\n",i);
        }

    }

    return 0;
}
