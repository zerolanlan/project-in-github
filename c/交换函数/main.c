#include <stdio.h>
#include <stdlib.h>



void change(int *,int *);
int main()
{
    int num1=5;
    int num2=10;
    change(&num1,&num2);
    printf("num1=%d,num2=%d",num1,num2);
}
void change(int *num1,int *num2)
{
    int b;
    b=*num1;
    *num1=*num2;
    *num2=b;
}
