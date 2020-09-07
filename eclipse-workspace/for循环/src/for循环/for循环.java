package for循环;

public class for循环 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int i,j;							//定义两个循环变量
		itcast: for (i=1;i<=9;i++) {		//外层循环
			for(j=1;j<=i;j++) {				//内层循环
				if(i>4) {					//判断i的值是否大于4
					break itcast;			//跳出循环
				}
				System.out.print("*");	//打印*
			}
			System.out.print("\n");		//换行
		}
		
	}

}
