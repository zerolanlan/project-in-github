package 数组;

import java.util.Random;

public class BubbleSort {
		// TODO Auto-generated method stub
		public static void bubbleSort(int[] arr){
			int i,j,t;
			//1.数组初始化，打印输出
			for(i=0;i<arr.length;i++){
				arr[i]=new Random().nextInt(100);
			}
			for(i=0;i<arr.length;i++){
				System.out.print(arr[i]+" ");
			}
			System.out.println();
			
			//2.冒泡排序
			for(j=1;j<arr.length;j++){
				for(i=0;i<arr.length-j;i++){
					if(arr[i]>arr[i+1]){
						t=arr[i];
						arr[i]=arr[i+1];
						arr[i+1]=t;
					}
				}
			}
			
			//3.排序之后打印输出
			for(i=0;i<arr.length;i++){
				System.out.print(arr[i]+" ");
			}
		}
		
		public static void main(String[] args) {
			int[] arr = new int[10];
			bubbleSort(arr);
		}
	
}




	


