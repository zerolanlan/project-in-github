package 类的继承;

class Animal {
	String name;//定义name属性
	//定义动物叫的方法
	void shout() {
		System.out.println("动物发出的声音");
	}
}
//定义Dog类继承Animal类
class Dog extends Animal {
	//定义一个打印name的方法
	public void printName() {
		System.out.println("name=" + name);
	}
}
//定义测试类
public class 概念 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Dog dog = new Dog();//创建一个Dog类的实例对象
		dog.name = "沙皮狗";//为Dog磊的name属性赋值
		dog.printName();//调用dog类的getInfo()方法
		dog.shout();//调用dog类的继承来的shout()方法
	}

}
