#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a[]={8,4,2,1,23,344,12};
    int sum=0;
    double avg;

    for{int i=0;i<7;i++}{
       printf("%d",a[i]);
       sum+=a[i];
    }
     printf("\n总和为；%d",sum);
     avg=sum/7.0;
    printf("平均值为；%.2f\n",avg);
    return 0;
}
