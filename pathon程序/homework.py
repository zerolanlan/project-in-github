float fenzi=0,fenmu=0;
        float shang=0,cha=0;
        float mincha=40;
        int answerfenzi=0,answerfenmu=0;
        for(fenmu=1;fenmu<=20;fenmu++){
            for(fenzi=1;fenzi<=20;fenzi++){
                if(fenzi%2==0&&fenmu%2==0)
                    continue;
                shang=fenzi/fenmu;
                cha=shang-0.618f;
                cha=cha<0?0-cha:cha;//转换成绝对值
                if(cha<mincha){
                    mincha=cha;
                    answerfenzi=(int)fenzi;
                    answerfenmu=(int)fenmu;
                }
            }
        }
        System.out.println("分子"+answerfenzi+"分母"+answerfenmu);
    }


	}
