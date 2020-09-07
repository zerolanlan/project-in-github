package 抽象类和接口;

public class usb接口2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Computer c = new Computer();
		//想计算机添加鼠标·麦克风·键盘设备
		c.add(new Mouse());
		c.add(new Mic());
		c.add(new KeyBoard());
		c.powerOn();//关闭计算机
		System.out.println();
		c.powerOff();//关闭计算机
	}

}
