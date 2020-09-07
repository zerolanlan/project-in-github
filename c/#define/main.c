#include <stdio.h>
#define   PI 3.1415926

void main()
{
   int radius;       //变量定义；圆的半径
   float area;       //变量定义；圆的面积
   radius=10;        //半径赋初值
    area=PI*radius*radius;
    printf("area=%f",area);
}
