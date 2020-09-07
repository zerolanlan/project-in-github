package 构造方法;
class Outer{
	private static int num=4;//定义成员变量
	//下面的代码定义了一个成员方法，方法中包含内部类
	public void test() {
		Inner inner = new Inner();
		Inner.show();
	}
	//下面的代码定义了一个成员内部类
	static class Inner{
		static void show() {
			//在成员内部的方法种访问外部类的成员变量
			System.out.println("num =" + num);
		}
	}
}
public class 成员内部类 {

	public static void main(String[] args) {
		Outer outer = new Outer();//创建外部类对象
		outer.test();//调用test()方法
	}

}
