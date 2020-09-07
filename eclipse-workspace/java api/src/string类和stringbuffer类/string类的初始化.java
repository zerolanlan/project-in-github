package string类和stringbuffer类;

public class string类的初始化 {

	public static void main(String[] args) {
		// 创建一个空的字符串
		String strl = new String();
		//创建一个类容为abcd的字符串
		String str2 = new String("abcd");
		//创建一个类容为字符串组的字符串
		char[] charArray = new char[] {'D','E','F'};
		String str3 = new String(charArray);
		System.out.println("a" + strl +"b");
		System.out.println(str2);
		System.out.println(str3);
	}

}
