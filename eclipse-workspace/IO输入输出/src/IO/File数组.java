package IO;

import java.io.File;

public class File数组 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		File file = new File("D:\\test");//创建一个代表目录的File对象
		deleteDir(file);//调用deleteDir删除方法
		
	}
	public static void deleteDir(File dir) {
		if (dir.exists()) {	//判断传入的File对象是否存在
			File[]  files = dir.listFiles();//得到File数组
			for (File file : file) {  //遍历所有的子目录和文件
				if (file.isDirectory())  {
					deleteDir(file); // 如果是目录，递归周期用deleteDir（）
				}else {
					//如果是文件，直接删除
					file.delete();
				}				
			}
			//删除完一个目录里的所有文件后，就删除这个目录
			dir.delete();
		}
	}
}
