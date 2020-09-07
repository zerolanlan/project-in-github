package 数组;

public class student {
	static String  schoolName;
	String studentName;
	int age;
	void introduce() {
		System.out.println(studentName+"就读于"+schoolName+",今年"+age+"岁");
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		student s1 =new student();
		student s2 =new student();
		student.schoolName="学院";
		s1.studentName="张三";
		s1.age=25;
		s1.introduce();
		s2.introduce();
		
	}

}
