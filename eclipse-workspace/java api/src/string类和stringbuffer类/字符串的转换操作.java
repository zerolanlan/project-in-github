package string类和stringbuffer类;

public class 字符串的转换操作 {

	public static void main(String[] args) {
			// TODO Auto-generated method stub
		String str = "abcd";
		System.out.println("将字符串转化为字符数组后的结果：");
		char[] charArray = str.toCharArray();	//将字符串转化为字符数组
		for (int i = 0;i < charArray.length; i++);
			int i;
			if (i !=charArray.length - 1) {
				System.out.print(charArray[i]+",");
			}else {
				//数组的最后一个元素后面不加逗号
				System.out.println(charArray[i]);
			}			
	}
		System.out.println(String.valueOf(13));
		System.out.println(s.toUpperCase());
	}
