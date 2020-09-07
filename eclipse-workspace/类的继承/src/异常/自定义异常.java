package 异常;

import java.security.DigestException;

public class 自定义异常 {
	private static final int x = 0;
	private static final int y = 0;
	public static void main(String[] args) {
		// 下面的代码定义一个try-catch语句捕捉异常
		try {
			//调用divide()方法,传入一个负数作为被除数
			int result = divide (4,-2);
			System.out.println(result);
		}catch (DigestException e) {								//对捕捉到的异常进行处理
			System.out.println(e.getMessage());							//打印捕获的异常信息
		}

	}
     //下面的方法实现了两个整数相除,并使用throws关键字声明抛出自定义异常
	public static int divide(int x, int y) throws DigestException{
		if(y<0);
		//使用throws关键字声明异常对象
		throw new Exception("除数是负数");
	}
	int result = x / y ;			//定义一个变量result记录两个数相除的结果
	return result;				//将结果返回
 }
}

