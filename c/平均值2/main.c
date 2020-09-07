#include <stdio.h>
#include <stdlib.h>

int main()
{
    int input;
    int sum=0;
    double avg=0;

    for(int i=0; i<5;i++ ){
        printf("请输入第%d个正整数\n",i+1);
        scanf("%d",&input);
        if(input<0){
            printf("请输入正整数\n");
            i--;
            continue;
        }
        sum+=input;
    }

    avg=sum/5.0;
    printf("平均值为：%f\n",avg);

    return 0;
}
