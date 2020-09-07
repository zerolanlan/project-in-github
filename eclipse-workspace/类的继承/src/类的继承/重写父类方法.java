package 类的继承;
//定义animal类
class Animal {
	//定义动物的叫法
	void shout() {
		System.out.println("动物发出叫声");
	}
}
//定义Dog磊的继承动物类
class Dog extends Animal {
	//定义狗叫的方法
	void shout() {
		System.out.println("汪汪汪.....");
	}
}
//定义测试类
public class 重写父类方法 {

	public static void main(String[] args) {
		Dog dog = new Dog();//创建dog类的实例对象
		dog.shout();//调用dog重写的shout()方法
	}

}
