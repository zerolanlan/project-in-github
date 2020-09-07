package 对象创建使用;
	class Student01 {
		private String name;
		private int age;
		public String getName() {
			return name;
		}
		public void setName(String stuName) {
			name = stuName;
		}
		public int getAge() {
			return age;
		}
		public void setAge (int stuAge) {
			if(stuAge<=0) {
				System.out.println("对不起，你输入的年龄有误。。。");
			}else {
				age = stuAge;
			}
		}
		public void introduce() {
			System.out.println("大家好。我叫"+name+"，我今年"+age+"岁！");
		}
	}
	public class 类的封装1 {
		public static void main(String[]args) {
			Student01 stu = new Student01();
			stu.setAge(-30);
			stu.setName("韩强");
			stu.introduce();		
		}
}