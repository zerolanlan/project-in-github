#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a[6]={3,6,9,12,15,18};
    int *p1 = &a[0];                              // 指向数组的第一个元素下标
    int *p2 = &a[5];                              // 求出最后一个元素的下标

    while (p1 < p2)
{
    int tmp = *p1;
    *p1 = *p2;
    *p2 = tmp;
    *p1++,*p2--;
}
    int i;
    for (i = 0; i < 6; i++)
{
    printf ("%4d", a[i]);
}
    printf ("\n");
    return 0;
}


