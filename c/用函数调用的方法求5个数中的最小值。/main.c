#include <stdio.h>
#include <stdlib.h>

int main()
 {
int b,a,min;
   printf("输入五个数，找出其中的最小值：\n");
     scanf("%d",&a);
      min=a;
for(b=0;b<4;b++)
{
    scanf("%d",&a);
if(min>a) min=a;
}
   printf("这五个数中，最小值是：%d",min);
    return 0;
}

