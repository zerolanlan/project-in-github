#include <stdio.h>
#include <stdlib.h>
main()
{
         int n;
         int fact(int);//实现阶乘的函数
         printf("Input n:");
         scanf("%d",&n);
         printf("%d!=%d\n",n,fact(n));
}
int fact(int n)
{
         int pro=1;
         int m=1;
         for(;m<=n;++m)
                   pro=pro*m;
         return(pro);
}
