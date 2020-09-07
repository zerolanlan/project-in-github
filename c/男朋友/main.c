#include <stdio.h>
#include <stdlib.h>

int main()
{
    int total=0;
    int choise;

    printf("男；你先睡，我和朋友开黑打游戏。\n");
    printf("女；都几点了还打。\n");
    printf("男；乖，你先睡嘛。\n");
    printf("女：算了，反正游戏比我重要，朋友也比我重要，你就去玩吧!\n");
    printf("男；好勒。\n");
    printf("请问接下来这女生会干嘛？\n");
    printf("请问接下来这女生会干嘛？\n");
    printf("1：和男朋友说晚安\n");
    printf("2：继续和男朋友聊下去\n");
    printf("3；生男朋友的闷气\n");
    printf("4；和男朋友一起开黑打游戏\n");
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
    printf("女友和你吵架了，一气之下，说让你滚，此刻你应该怎么办?\n");
    printf("1：先离开，让女朋友冷静一下，过后再哄\n");
    printf("2：立刻低头和女朋友道歉\n");
    printf("3；抱住她，和她说我滚了，你怎么办？\n");
    printf("4：和她讲道理，让她给出滚的理由\n");

    scanf("%d",&choise);

    switch(choise){
case 1:
    total+=0;
    break;
case 2:
    total+=10;
    break;
case 3:
    total+=20;
    break;
case 4:
    total+=0;
    break;
    }

    printf("目前得分：%d\n",total);
    printf("三：送命题 满分五十分\n");
    printf("女友处于减肥期间，但她又很想吃高热量食物，你应该怎么办？\n");
    printf("1:让她吃，过后再让她减肥\n");
    printf("2:和她说，你又不胖，吃这点东西怎么了\n");
    printf("3:不能给她吃，告诉她这样会前功尽弃\n");
    printf("4:陪她吃，过后两人一起减肥");
    scanf("%d",&choise);

    switch(choise){
case 1:
    total+=0;
    break;
case 2:
    total+=10;
    break;
case 3:
    total+=10;
    break;
case 4:
    total+=30;
    break;
    }


    printf("四；致命题，满分五十分\n");
    printf("某次，你惹女友生气了，然后你和她不断道歉。她说，你怎么连这点脾气都没有。你说因为你，我早就没有脾气了。她破涕为笑，说让你骂她一下试试，结果你骂了她。女友对你说：你居然敢对我发火，这么多年你从来没有大声说过我，现在居然骂我，你会后悔的，你接着说，你不是希望我骂一下你试试吗？女友说，我让你骂你就骂啊，你是猪啊！");
    printf("1:希望，因为她要求了，但是要赞美地骂\n");
    printf("2:希望，因为她嫌弃你没有脾气\n");
    printf("3:不希望，因为她就是喜欢你没有脾气\n");
    printf("4:不希望，因为你就从没有大声说过她\n");
    scanf("%d",&choise);

    switch(choise){
case 1:
    total+=30;
    break;
case 2:
    total+=0;
    break;
case 3:
    total+=10;
    break;
case 4:
    total+=10;
    break;

    printf("目前得分：%d\n",total);
    return 0;
    }
}


