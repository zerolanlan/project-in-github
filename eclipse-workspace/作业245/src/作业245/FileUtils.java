package 作业245;
import java.awt.RenderingHints.Key;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FilenameFilter;
import java.util.ArrayList;

public class FileUtils {

	public static ArrayList<String> listFiles(File file,final String key) {
		FilenameFilter filter = new FilenameFilter() {
			public boolean accept(File dir, String name) {
				File currFile = new File(dir,name);
				//如果文件名包含关键字返回true,否则返回false
				if (currFile.isFile() && name.contains(key)) {
					return true;
				}
				return false;
			}
		};
		//递归方式获取规定路径
		ArrayList<String> arrayList = fileDir(file,filter);
		return arrayList;
	}
	/**
	 * 指定后缀名检索文件
	 * @param suffixArray 后缀名数组
	 * @return 指定后缀名的文件路径
	 */
	public static ArrayList<String> listFiles(File file,final String[] suffixArray) {
		FilenameFilter filter = new FilenameFilter() {
			public boolean accept(File dir, String name) {
				File currFile = new File(dir,name);
				if (currFile.isFile()) {
					for(String suffix : suffixArray) {
						if (name.endsWith("." + suffix)) {
							return true;
						}
					}
				}
				return false;
			}
		};
		//递归方式获取规定的路径
		ArrayList<String> arraylist = fileDir(file,filter);
		return arraylist;
	}
	/** 递归方式获取规定的路径
	 *@param dir File 对象
	 *@param filter过滤器
	 *@return 过滤器过滤后的文件路径
	 */
	public static ArrayList<String> fileDir(File dir, FilenameFilter filter) {
		ArrayList<String> arraylist = new ArrayList<String>();
		File[] lists = dir。listFiles(filter); // 获取过滤后的所有文件数组
		for (File list : lists) {
			//将文件的绝对路径放到集合里面
			arraylist.add(list.getAbsolutePath());
		}
		File[] files = dir.listFiles(); //获取当前目录下所有文件的数组
		for (File file : files) {  //遍历所有的子目录和文件
			if (file.isDirectory()) {
				//如果是目录，递归调用fileDir()
				ArrayList<String> every = fileDir(file, filter);
				arraylist.addAll(every);//将文件夹下的文件路径添加到集合当中
			}
		}//此时的集合中有当前目录下的文件路径，和当前目录的子目录下的文件路径
		return arraylist;
	}
	/*
	 * 复制文件/目录
	 * @param srcFile 源目录
	 * @param destFile 目标目录
	 */
	public static void copySrcPathToDestPath(File srcDir,File destDir) throws Exception{
		File[] files = srcDir.listFiles();//子文件目录
		for(int i = 0; i < files.length; i++) {
			File copiedFile = new File(destDir, files[i].getName());
			if (files[i].isDirectory()) { //如果是目录
				if (!copiedFile.mkdir()) {//创建文件夹
					System.out.println("无法创建："+copiedFile);
					return;
				}
				//调用递归，获取子文件下的文件路径
				copySrcPathToDestPath(files[i],copiedFile);
			}else {//复制文件
				FileInputStream input = new FileInputStream(files[i]);
				FileOutputStream output = new FileOutputStream(copiedFile);//获取输出流
				byte[] buffer = new byte[1024];//创建缓冲区
				int n = 0;
				//循环读取字节
				while ((n = input.read(buffer))!=-1) {
					output.write(buffer, 0, n);
				}
				input.close();//关闭输入流
				output.close();//关闭输出流
			}
		}
	}
}


