#include <stdio.h>
#include <stdlib.h>

void main()
{
    char ch1,ch2,ch3,ch4,ch5;
    ch1='H';ch2='e';ch3='l';ch4='l';ch5='0';
    printf("加密前的字符是；%c%c%c%c%c\n",ch1,ch2,ch3,ch4,ch5);
    ch1=ch1+3;
    ch2=ch2+6;
    ch3=ch3+2;
    ch4=ch4+4;
    ch5=ch5+4;
    printf("加密后的字符是；%c%c%c%c%c\n",ch1,ch2,ch3,ch4,ch5);
}
