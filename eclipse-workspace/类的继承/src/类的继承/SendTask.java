package 类的继承;
public class SendTask {
		private String goodsWeight;
		private String sendNumber;
		private String number;
		private Object goodWeight;
		public String getGoodsWeight() {
			return goodsWeight;
		}
		public void setGoodsWeight(String goodsWeight) {
			this.goodsWeight = goodsWeight;
		}
		public String getSendNumber() {
			return sendNumber;
		}
		public void setSendNumber(String sendNumber) {
			this.sendNumber = sendNumber;
		}
		
		public SendTask(){
			super();
		}
		public SendTask(String goodWeight,String sendNumber){
			this.goodsWeight=goodWeight;
			this.sendNumber = sendNumber;
		}
		
		//运输前
		public void sendBefore(){
			System.out.println("订单开始处理，仓库验货中...");
			System.out.println("货物的重量为："+goodsWeight);
			System.out.println("货物验货完毕！");
			System.out.println("货物装载完毕！");
			System.out.println("运货人已通知！");
			System.out.println("快递单号为："+sendNumber);
		}
		
		
		//运输中
		public <GPS> void send(Trasportation t,GPS tool){
			System.out.println("运货人"+t.Getadmin()+"正在驾驶编号为"+t.Getnumber()+"的"+t.getModel()+"运输货物...");
			t.transport();
			String showCoodinate = tool.showCoordinate();
			System.out.println("当前坐标为："+showCoordinate);
		}
		
		//运输后
		public void sendAfter(Trasportation t){
			System.out.println("运输任务已经完成！");
			System.out.println("运货人"+t.Getadmin()+"驾驶的编号为"+t.Getnumber()+"的"+t.getModel()+"已经归还！");	
		}
		public String getNumber() {
			return getNumber();
		}
		public void setNumber(String number) {
			this.number = number;
		}
		public double getGoodweight() {
			return getGoodweight();
		}
		public void setGoodWeight(double goodweight) {
			this.goodWeight = goodWeight;
		}
}
		

