package 类的继承;

public abstract class Trasportation {
	private String number; //编号
	private String model;  //型号
	private String admin; //运货负责人
	public void Transportion()	{
	}
	public Trasportation(String number, String model, String admin) {
		this.number = number;
		this.model = model;
		this.admin = admin;
	}
	//运输方法
	public abstract void transport();
	//编号
	public void setNumber(String number) {
		this.number = number;
	}
	public String Getnumber() {
		return number;
	}
	//型号
	public void setModel(String model) {
		this.model = model;
	}
	public String getModel() {
		return model;
	}
	//负责人
	public void setAdmin(String admin) {
		this.admin = admin;
	}
	public String Getadmin() {
		return admin;
	}
}
