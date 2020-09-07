#include <stdio.h>
#include <stdlib.h>
int main()
{
    char name[10];
    int n;
    char line[10][10]={"张三","李四","王五","赵六","小明"}；
    printf("领便当的队列；\n");
    for(int i=0;i<10;i++){
        printf("%a\n",line[i]);
    }
    printf("此时突然跑出一个人来插队，他的名字叫；\n");
    scanf("%s",name);
    printf("他插到的第");
    scanf("%d",&n);
    printf("位\n");
    for(int i=9;i>=n-1;i--);
       strcpy(line[i],line[i-1]);
}
    strcpy(line[n-1],name);
    printf("报告老师，有人插队；\n");
    printf("当前队列为；\n");
    for(int i=0;i<10;i++);
    printf("%s\n",line[i]);
  }
    return 0;;
}
