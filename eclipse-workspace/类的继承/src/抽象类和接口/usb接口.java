package 抽象类和接口;

import javax.jws.soap.SOAPBinding.Use;

public class usb接口 {
	private usb接口[] usbArr = new usb接口[4];

	public Use[] getUsbArr(Use[] usb接口) {
		return usb接口;
	}
	public void setUsbArr(usb接口[] usbArr) {
		this.usbArr = usbArr;
	}
	
	public void add(usb接口 usb){
		for(int i=0;i<usbArr.length;i++){
			if(usbArr[i]==null){
				usbArr[i]=usb;
				break;
			}
		}
	}
	
	public void powerOn(){
		for(int i=0;i<usbArr.length;i++){
			if(usbArr[i]!=null){
				usbArr[i].turnOn();
			}
		}
		System.out.println("计算机已经开机！");
	}
	
	private void turnOn() {
		// TODO Auto-generated method stub
		
	}
	public void powerOff(){
		for(int i=0;i<usbArr.length;i++){
			if(usbArr[i]!=null){
				usbArr[i].turnOff();
			}
		}
		System.out.println("计算机已经关机！");
	}
	private void turnOff() {
		// TODO Auto-generated method stub
		
	}
}


