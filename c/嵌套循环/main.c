#include <stdio.h>
#include <stdlib.h>

void main()
{
    int i;
    int k;
    for(k=1;k<=100;k++){
        i=2;
        while(i<=k);
        if(k%i==0){
            break;
        }
        i++;
    }
    if(i==k){
        printf("%d\n",k);
    }else{
        //printf("%d²»ÊÇËØÊý\n",k);
    }
  }
    return 0;
}
