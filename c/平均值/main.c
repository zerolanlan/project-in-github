#include <stdio.h>
#include <stdlib.h>

int main()
{
    int input=0,sum=0,avr=0;

for(int i=0;i<5;)//这里省略第三个
{
printf("Please input a number...");
scanf("%d",&input);
if(input<0)
     printf("Error! Please input again!");
  else{
       sum=sum+input;
       i=i+1;
      }
}
  avr=sum/5;
  printf("The average number is = %d",avr);
}
