#include <stdio.h>
#include <stdlib.h>

int main()
{   int num1=1024;
    int num2=2048;
    int *ptr1;
    int *ptr2;
    ptr1= &num1;
    ptr2= &num2;
    printf("num1的值为；%d\tptr1指向；%p\n",num1,ptr1);
    printf("num2的值为；%d\tptr2指向；%p\n",num2,ptr2);
    ptr2=ptr1;
    //*ptr2=*ptr1;
    printf("重新赋值后；\n");
    printf("num2的值为；%d\tptr2指向；%p\n",num2,ptr2);


    return 0;
}
