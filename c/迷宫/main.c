 #include <graphics.h>
 #include <stdlib.h>
 #include <bios.h>   /*定义几个功能按键*/
 #define ESC 0x11b      /*强行退出游戏*/
 #define UP 0x4800      /*上下左右四个按键移动小人*/
 #define DOWN 0x5000
 #define LEFT 0x4b00 #define RIGHT 0x4d00  int a[50][50]={0}; /* 存放地图信息的数组  0：不可走的障碍物 1：可以走的路  */
 int qdx=1,qdy=1,zdx=20,zdy=20;  /* 起点和终点的坐标 */
 int renx,reny;   /* 小人坐标  */
 int d=20;    /* 小格子的间距 */
 int kk=0,rr=2;   main() {
     int i,j,m=30,n=16,d=20,k;
     int gdriver = DETECT, gmode;
     randtu(200);
     renx=qdx,reny=qdy;
     registerbgidriver(gdriver);
     initgraph(&gdriver, &gmode, "c:\\turboc2");
     redraw();
     while(1)              /* 反复从键盘获得程序需要的按键 */
        {     if(bioskey(1))         /* 判断是否有按键 */
        {        k=bioskey(0);       /* 将按键存入变量k */
     switch(k)           /* 对按键进行分情况处理 */
     {    case ESC:            /* ESC键 退出 */
         printf("%d times\n",kk);
          exit(0); break;    case UP:             /* UP键向上移动光标 */
              if(a[renx][reny-1]==1)
                {           reny-=1;
              redraw();        }

       break;
       case DOWN:           /* DOWN键向下移动光标 */
           if(a[renx][reny+1]==1)
            {           reny+=1;
           redraw();        }
           break;
           case LEFT:           /* LEFT键向左移动光标 */
               if(a[renx-1][reny]==1)
                {           renx-=1;
               redraw();        }
               break;
               case RIGHT:          /* RIGHT键向右移动光标 */
                   if(a[renx+1][reny]==1)
                    {           renx+=1;
                   redraw();        }
                   break;
                    }
                    }
                    }
                    getch();
                    closegraph(); } /*      redraw重画函数在用户有操作后，重画游戏画面 */
                    redraw()
           {
               int i,j;
               for(i=qdx;i<=zdx;i++)
                for(j=qdy;j<=zdy;j++)
                {
                    if(i<renx+rr && i>renx-rr && j<reny+rr && j>reny-rr)
                    if(a[i][j]==0)   geziza(i*d,j*d);
                else          gezilu(i*d,j*d);
                else                gezibk(i*d,j*d);    }
                drawren(renx*d,reny*d); }  /*           随机地图（randlei）函数用于随机生成地图 */
                randtu(int num) {
                    int i,j,xx,yy,sum,t,m,n;
                    srand(time(NULL)); loop: sum=0;
                    m=zdy-qdy+1;  n=zdx-qdx+1;  a[qdx][qdy]=1;  a[zdx][zdy]=1;
                    do
                    {      t=random(m*n);      xx=t/m+1;      yy=t%m+1;
                    if(a[xx][yy]==0)
                        {          a[xx][yy]=1;
                    sum++;   }
                    }while(sum<num);
                    if(ok()) return;
                    for(i=0;i<50;i++)
                        for(j=0;j<50;j++)
                        a[i][j]=0;
                    kk++;
                    goto loop; } ok()  {
                        int b[50][50]={0};
                         b[qdx][qdy]=1;
                         tansuo(qdx,qdy,b);
                         return(b[zdx][zdy]); }
                         tansuo(int x,int y,int *b[50][50]) /* 如果当前格子为空白无雷情况，向周围探索相类似的情况，
