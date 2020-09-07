#include <stdio.h>
#include <stdlib.h>

int main()
{
    double score{2}{3} = {{98,87,65},{54,43,21}};
    double {*ptr_score}{3}; //**ptr_score
    ptr_score = score;
    for(int i=0;i<2;i++){
            for(int j=0;j<3;j++){
              printf("%.2f\n",*(*(ptr_score+i)+j));
     }
     //printf("%.2f\n",*ptr_score++);
     //printf("%.2f\n",ptr_score[i]);
     //printf("%.2f\n",*ptr_score+j));
    }
    return 0;
