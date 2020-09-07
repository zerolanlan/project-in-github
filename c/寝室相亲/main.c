#include <stdio.h>
#include <stdlib.h>

int main()
{   int a[8]={55,60,65,62,68,70,80,75};
    int b[8]={170,172,173,174,175,176,178,180,};
    int c,d,e,f,g,h,i,j;
    printf("若有符合要求的显示“存在”，反之则不显示\n");
    printf("请输入理想的体重(单位；kg)；");
    scanf("%d",&c);
    for(i=0;i<8;i++){
        if(c==a[i]){
                printf("存在\n");
                break;
        }
}
    printf("请输入理想的身高(单位；cm)；");
    scanf("%d",&d);
    for(i=0;i<8;i++){
        if(d==b[i]){
                printf("存在\n");
                break;
        }
}
    printf("请输入理想型的体重范围(中间为“-”)；");
    scanf("%d-%d",&e,&f);
    for(i=0;i<8;i++){
        if(e>=a[i]){
            for(j=0;j<8;j++){
                    if(f<=a[j]){
                            printf("存在\n");
                            break;
        }
}
     printf("请输入理想型的身高范围(中间为“-”)；");
     scanf("%d-%d",&g,&h);
     for(i=0;i<8;i++){
        if(e>=b[i]){
            for(j=0;j<8;j++){
                    if(f<=b[j]){
                            printf("存在\n");
                            break;
        }

}
        }
     }
        }
    }
}
