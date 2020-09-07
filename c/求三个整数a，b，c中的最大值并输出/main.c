#include <stdio.h>
#include <stdlib.h>

void main()
{
       printf("input number\n");
       int a,b,c;
       scanf("%d %d %d",&a,&b,&c);
       int max =a ;
       if(max < b) max =b;
       if(max< c) max =c;
       printf("max =%d\n",max);
}
