#include <stdio.h>
#include <stdlib.h>

int main()
{
    int max=0;
    int min=0;
    int input;

    for(int i=0;i<8;i++){
            scanf("%d",&input);

            if(i==0){
                    max=min=input;
            }
            if(input>max){
                    max>input;
            }
            if(input<min){
                    min=input;
            }
    }
         printf("最大值为；%d，最小值为；%d\n",max,min);
}
