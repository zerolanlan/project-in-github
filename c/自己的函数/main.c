#include <stdio.h>
#include <stdlib.h>

double circleArea(double);
int main()
{
    double radio;
    printf("请输入圆的半径：");
    scanf("%lf",&radio);
    //double area=circleArea(radio);
    printf("\n半径为%f的圆的面积为%f",radio,circleArea(radio));
    return 0;
}
//函数定义
double circleArea(double r){
    double s=3.1315*r*r;
    return s;
    }
