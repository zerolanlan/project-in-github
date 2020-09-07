package 数组;

public class zuoye3 {
	String name;//成员变量
	int age;//定义成员变量
	
	void speak() {
		System.out.println(name+age);//输出姓名和年龄
	}
	
	public static void main(String[] args) {
		zuoye3 p1 = new zuoye3();//生成对象p1
		zuoye3 p2 = new zuoye3();//生成对象p2
		p1.name="zhangsan";//给对象p1的name变量赋值
		p1.name="lisi";//给对象p2的name变量赋值
		p1.age=25;//给对象p1的age变量赋值
		p2.age=30;//给对象p2的age变量赋值
		p1.speak();//调用对象p1的成员方法speak
		p2.speak();//调用对象p2的成员方法speak
	}
}
