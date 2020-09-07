package 抽象类和接口;
//定义Animal类
class Animal {
	//动物叫的方法
	void shout() {
		System.out.println("动物叫！");
	}
}
//定义测试类
public class object类 {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
			Animal animal = new Animal();				//创建Animal类对象
			System.out.println(animal.toString());		//调用toString()方法并打印
	}
}
