#include <stdio.h>
#include <stdlib.h>

int main()
{
    float hurt;   //伤害
    float armor;    //护甲
    float life;     //生命值
    float mana;     //法力
    float   speed;    //移速
    int   coupons;  //点券
    int   distance; //攻击距离
    float magic_resistance;    //魔抗
    float life_regen;    //生命回复
    float mana_regeneration;   //魔力回复
    int   gold_coin;     //金币


    hurt=57.88;armor=756.22;life=616.28;mana=0.0;speed=340.23;coupons=450;distance=172;magic_resistance=96.99;life_regen=36.23;mana_regeneration=56.22;gold_coin=331;
    printf("名称:蒋光超超神\n");
    printf("伤害:%.2f      护甲:%.2f\n",hurt,armor);
    printf("生命值:%.2f    法力:%.2f\n",life,mana);
    printf("移速:%.2f      点券:%d\n",speed,coupons);
    printf("攻击距离:%d    魔抗:%.2f\n",distance,magic_resistance);
    printf("生命恢复:%.2f  魔力回复:%.2f\n",life_regen,mana_regeneration);
    printf("金币:%d        定位:肉盾 抗塔 进攻\n",gold_coin);
    return 0;
}
