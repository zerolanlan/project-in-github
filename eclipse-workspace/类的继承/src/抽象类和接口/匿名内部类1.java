package 抽象类和接口;
//定义动物类接口
interface Animal {	//定义动物类接口
	void shout();	//定义方法shout()
}
public class 匿名内部类1 {

	public static void main(String[] args) {
		// 定义匿名内部类作为参数传递给animalShout()方法
		animalShout(new Animal(){
			//实现shout()方法
			public void shout() {
				System.out.println("喵喵、、、、");
			}
		});
	}
		//定义静态方法animalShout()
		public static void animalShout(Animal an) {
			an.shout(); //调用传入对象an的shout()方法
			}
}
