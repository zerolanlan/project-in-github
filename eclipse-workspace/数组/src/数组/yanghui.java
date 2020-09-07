package 数组;

public class yanghui {

	public static void yangHui(int[][] args) {
		// TODO Auto-generated method stub
		int i,j;
		//第一列和对角线赋值
		for(i=0;i<args.length;i++){
			args[i][0]=1;
			args[i][i]=1;
		}
		//2.其他元素赋值
		for(i=2;i<args.length;i++){
			for(j=1;j<i;j++){
				args[i][j]=args[i-1][j-1]+args[i-1][j];
			}
		}
		//3.输出
		for(i=0;i<args.length;i++){
			for(j=0;j<=i;j++){
				System.out.print(args[i][j]+" ");
			}
			System.out.println();
		}	
	}
	public static void main(String[] args){
		int[][] arr = new int[8][8];
		yangHui(arr);
	}
}

	


