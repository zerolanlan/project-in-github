package 作业245;
import java.util.LinkedList;
import java.util.Scanner;
public class KTVByLinkedList {

	public static void main(String[] args) {
		System.out.println("---------欢迎来到点歌系统---------");
		System.out.println("0.添加歌曲至列表");
		System.out.println("1.将歌曲置顶");
		System.out.println("2.将歌曲前移一位");
		System.out.println("3.退出");
		LinkedList<String> lineUpList = new LinkedList<String>();//创建歌曲列表
		addMusicList(lineUpList);//添加一部分歌曲至歌曲列表
		while (true) {
			System.out.println("请输入要执行的操作序号");
			java.util.Scanner scan = new Scanner(System.in);
			int command = scan.nextInt();// //接受键盘输入的功能选项序号
			//执行序号对应的功能
			switch (command) {
			case 0://添加歌曲至列表
				addMusic(lineUpList);
				break;
			case 1://将歌曲置顶
				setTop(lineUpList);
				break;
			case 2://将歌曲前移一位
				setBefore(lineUpList);
				break;
			case 3://退出
				exit();
				break;
			default:
				System.out.println("------------------");
				System.out.println("功能选择有误,请输入正确的功能序号！");
				break;
			}
			System.out.println("当前歌曲列表：" + lineUpList);
		}
	}
//初始时添加歌曲名称
private static void addMusicList(LinkedList<String> lineUpList ) {
	lineUpList.add("稻香");
	lineUpList.add("夜曲");
	lineUpList.add("夜的第七章");
	lineUpList.add("听妈妈的话");
	lineUpList.add("龙卷风");
	System.out.println("初始歌曲列表" + lineUpList);
}
//执行添加歌曲
private static void addMusic(LinkedList<String> lineUpList) {
	System.out.print("请输入要添加的歌曲吗名称：");
	String musicName = new Scanner(System.in).nextLine();
	lineUpList.addLast(musicName);//添加歌曲到列表的最后
	System.out.println("已添加歌曲：" + musicName);
}
//执行将歌曲置顶
private static void setTop(LinkedList<String> lineUpList) {
	System.out.print("请输入要置顶的歌曲名称");
	String musicName = new Scanner(System.in).nextLine();
	int position = lineUpList.indexOf(musicName);//查找指定歌曲位置
	if (position<0) {//判断输入歌曲是否存在
		System.out.println("当前列表中没有输入的歌曲！");
	}else {
		lineUpList.remove(musicName);//移除指定的歌曲
		lineUpList.addFirst(musicName);//将指定的歌曲放到第一位
	}
	System.out.println("已将歌曲" + musicName +"置顶");
}
//执行将歌曲置前一位
private static void setBefore(LinkedList<String> lineUpList) {
	System.out.print("请输入要置顶的歌曲名称");
	String musicName = new Scanner(System.in).nextLine();
	int position = lineUpList.indexOf(musicName);//查找指定歌曲位置
	if (position<0) {//判断输入歌曲是否存在
		System.out.println("当前列表中没有输入的歌曲！");
    }else if (position == 0){//判断歌曲是否已在第一位
	System.out.println("当前歌曲已在最顶部！");
    }else {
	lineUpList.remove(musicName);//移除指定的歌曲
	lineUpList.add(position - 1,musicName);//将指定的歌曲放到前一位
    }
    System.out.println("已将歌曲" + musicName + "置顶");
}	
//退出
private static void exit() {
	System.out.println("------------退出------------");
	System.out.println("您已退出系统");
	System.exit(0);
}
	
}
	
	