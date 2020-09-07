package string类和stringbuffer类;

public class 字符串的基本操作 {

	public static void main(String[] args) {
		String s ="ababcdedcba";//声明字符串
		System.out.println("字符串的长度为：" + s.length());//获取字符串长度，即字符个数
		System.out.println("字符串中的第一个字符：" + s.charAt(0));
		System.out.println("字符c第一次出现的位置：" + s.indexOf('c'));
		System.out.println("字符串最后一次出现的位置："+ s.indexOf('c'));
		System.out.println("子字符串第一次出现的位置："+ s.indexOf("ab"));
		System.out.println("子字符串最后一次出现的1位置：" + s.indexOf("ab"));
	}

}
