package 对象创建使用;

public class 超市购物系统 {

	public static void main(String[] args) {
		// 创建商品对象，给名字赋值
		Product p1 = new Product();
		Product p2 = new Product();
		Product p3 = new Product();
		Product p4 = new Product();
		Product p5 = new Product();
		p1.setProName("电视机");
		p2.setProName("电视机");
		p3.setProName("电视机");
		p4.setProName("电视机");
		p5.setProName("电视机");
		//创建超市对象，给超市名字赋值，给仓库赋值
		Market m = new Market();
		m.setMarketName("家乐福");
		m.setProductArr(new Product[] {p1,p2,p3,p4,p5});
		//创建人对象，给名字赋值
		Person p = new Person();
		p.setName("小韩");
		//调用购物方法，指定超市和商品名，得到购物结果
		Product result = p.shopping(m,"豆浆机");
		//根据结果进行判断
		if (result != null) {
			System.out.println(p.shopping() +"在"+ m.getMarketName() + "买到了" + result.getProName());			
		}else {
			System.out.println(p.getName() + "白跑一趟，在" + m.getMaketName() + "什么都没买到");
		}
		
	}

}