package AWT概述;
import java.awt.*;
public class FlowLayout {

	public static void main(String[] args) {
		final Frame f = new Frame("FlowLayout");
        //设置布局管理器为FlowLayout，所有组件左对齐，水平间距为20，垂直间距为30
		f.setLayout(new FlowLayout(FlowLayout.LEFT,20,30));
		f.setSize(220,300);
		f.setLocation(300,200);
		f.add(comp, constraints);
	}

}
