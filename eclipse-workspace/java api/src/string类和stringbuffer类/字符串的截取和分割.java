package string类和stringbuffer类;

public class 字符串的截取和分割 {

	public static void main(String[] args) {
		String str = "羽毛球-乒乓球-篮球";
		//下面是字符串截取操作
		System.out.println("从第5个字符截取到末尾的结果："+str.substring(4));
		System.out.println("从第5个字符截取到第6个字符的结果："+str.substring(4, 6));
	//下面是字符串分割的操作
		System.out.println("分割后的字符串数组中的元素依次为：");
		String[] strArray = str.split("-");		//将字符串转化为字符串数组
		for (int i = 0;i<strArray.length;i++) {
			//如果不是数组的最后一个元素，在元素后面加逗号
			System.out.print(strArray[i] + ",");
		 {
		//数组的最后一个元素，在元素后面加逗号
			System.out.println(strArray[i]);

	}

		}
	}
}

