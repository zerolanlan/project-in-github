package 抽象类和接口;
//定义animal接口
interface Animal{
	void shout(); 	//定义抽象方法shout()
}
//定义测试类
public class 匿名内部类 {

	public static void main(String[] args) {
		// 定义一个内部类cat实现Animal接口
	class Cat implements Animal {
		//实现shout方法
		public void shout() {
			System.out.println("喵喵....");
		}
		
	}
		animalShout(new Cat());  //调用animalShout()方法并传入Cat对象	
	}
	//定义静态方法animalShout（）
	public static void animalShout(Animal an) {
		an.shout();//调用传入对象an的shout()方法
	}

}
