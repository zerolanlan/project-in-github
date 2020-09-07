#include <stdio.h>
#include <stdlib.h>

int main()
{
    int choise;
    char names[8][10]={"杜能","刘智强","袁瑞","文岚清","蒋光超","刘家磊","张玉林","马林"};
    printf("今晚到场的嘉宾有：\n");
    for(int i=0;i<8;i++){
        printf("%d号嘉宾：%s\n",i+1,names[i]);
    }
    printf("请选择你的心动男生：");
    scanf("%d",&choise);
    switch(choise){
        case 1:
            printf("你选择的心动男生是：%d号嘉宾 %s",choise,names[0]);
            break;
        case 2:
            printf("你选择的心动男生是：%d号嘉宾 %s",choise,names[1]);
            break;
        case 3:
            printf("你选择的心动男生是：%d号嘉宾 %s",choise,names[2]);
            break;
        case 4:
            printf("你选择的心动男生是：%d号嘉宾 %s",choise,names[3]);
            break;
        case 5:
            printf("你选择的心动男生是：%d号嘉宾 %s",choise,names[4]);
            break;
        case 6:
            printf("你选择的心动男生是：%d号嘉宾 %s",choise,names[5]);
            break;
        case 7:
            printf("你选择的心动男生是：%d号嘉宾 %s",choise,names[6]);
            break;
        case 8:
            printf("你选择的心动男生是：%d号嘉宾 %s",choise,names[7]);
            break;

    }
}
