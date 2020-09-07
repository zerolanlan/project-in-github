package 类的继承;

class Animal {
	String name = "动物";
	//定义动物叫的方法
	void shout() {
		System.out.println("动物发出的声音");
	}
}
//定义Dog类继承Animal类
class Dog extends Animal {
	String name = "犬类";
	//重写父类shout()的方法
	void shout() {
		super.shout();  //调用父类的成员方法
	}
	void printName() {
		System.out.println("name=" + super.name);
	}
}
//定义测试类
public class super关键字  {

	public static void main(String[] args) {
		Dog dog = new Dog();//创建一个Dog类的实例对象
		dog.printName();//调用dog类的getInfo()方法
		dog.shout();//调用dog类的继承来的shout()方法
	}

}