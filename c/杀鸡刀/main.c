#include <stdio.h>
#include <stdlib.h>

int main()
{
    int total=0;
    int choise;

    printf("本测试共有四个题，用于测试你的女朋友是否为国民好女友 满分一百分\n");
    printf("一；基础题 满分二十分\n");

    scanf("%d",&choise);

    switch(choise){
case 1:
    total+=0;
    break;
case 2:
    total+=0;
    break;
case 3:
    total+=20;
    break;
case 4:
    total+=5;
    break;
    }

    printf("目前得分：%d\n",total);
    printf("二：提升题 满分三十分\n");
    printf("男：宝贝你先睡吧，我要和基友开黑！\n");
    printf("女：又开黑？到底是开黑重要还是我重要！你说啊！\n");


    printf("问：上述男朋友说的开黑是指？\n");
    printf("1:男生其实是黑社会，这是一种黑道上的黑话\n");
    printf("2:男生要去美黑了，这样显得更有男人味。\n");
    printf("3:这是一种直男间惯有的社交方法。\n");
    printf("4:男生要约上几个人，一起打游戏了。\n");
    scanf("%d",&choise);

    switch(choise){
case 1:
    total+=0;
    break;
case 2:
    total+=0;
    break;
case 3:
    total+=0;
    break;
case 4:
    total+=30;
    break;
    }

    printf("目前得分：%d\n",total);
     printf("三：送命题 满分五十分\n");
    printf("一天，你带上狗狗，和老公一同出海垂钓，结果遭遇台风！你的老公和养了8年的狗狗都掉进了水里，不会游泳，靠你的限量版Lv包包而得救，但是限量版Lv包包无法同时支撑老公和狗狗的重量，眼看人和狗都要溺水了，情况万分危急！这时候，你该怎么办？\n");

    printf("1:让老公踹开狗狗，扶着包包获救。\n");
    printf("2让狗狗咬你老公，扶着包包获救:\n");
    printf("3:自己跳下水，拿回你的包包。\n");
    printf("4:打110\n");
    scanf("%d",&choise);

    switch(choise){
case 1:
    total+=25;
    break;
case 2:
    total+=50;
    break;
case 3:
    total+=0;
    break;
case 4:
    total+=10;
    break;
    }

    printf("目前得分：%d",total);
    return 0;
    }
