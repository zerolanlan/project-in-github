package 异常;

public class Throws关键字 {		

	public static void main(String[] args) throws Exception{
		// TODO Auto-generated method stub
		int result = divide(4,2);			//调用divide
		System.out.println(result);
	}
	//下面方法实现了两个整数相除，并使用throws关键字声明抛出异常
	public static int divide(int x,int y) throws Exception{
		int result = x / y;								//定义一个变量result记录两个数相除的结果
		return result;									//将结果返回
	}
}
