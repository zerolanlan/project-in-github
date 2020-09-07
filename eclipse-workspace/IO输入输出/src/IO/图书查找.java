package IO;
public class 图书查找 {
	int id;
	String name;
	double price;
	int number;
	double money;
	String Publish;
	public 图书查找(int id,String name,double price,int number,double money,String Publish) {
		this.id = id;
		this.name = name;
		this.price = price;
		this.number = number;
		this.money = money;
		this.Publish = Publish;
	}  //10~17行代码定义了一个有参的构造方法（用于对象的创建和初始化）
	public String toString() {
		String message = "图书编号："+id+"图书名称："+name+"出版社："+Publish+"单价："+price+"库存数量："+number;
		return message;
	}//18~21行重写了toString()方法，用于返回图书的详细信息
	public void setNumber(int number) {
		this.number=number;
	}//22~24定义了一个setNumber()方法，用于修改图书库存量
}

