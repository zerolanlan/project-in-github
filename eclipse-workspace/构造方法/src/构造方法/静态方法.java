package 构造方法;

class Person {
	public static void sayHello() { //定义静态方法
		System.out.println("hello");
	}
		}
class 静态方法{
	public static void main(String[] args) {
		//1.类名.方法的方式调用静态方法
		Person.sayHello();
		//实例化对象的方式来调用静态方法
		Person p = new Person();
		p.sayHello();
		

	}

}
