#include <stdio.h>
#include <stdlib.h>

int main()
{    float weapon_attack;
     int strength;
     float real_damage;

     printf("请输入武器攻击力和角色力量，中间用空格隔开\n");
     scanf("%f %d",&weapon_attack,&strength);
     real_damage = weapon_attack*(strength+100)/100;
     printf("角色实际伤害为；%.2f\n",real_damage);
    return 0;
}
