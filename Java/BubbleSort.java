

import java.util.Scanner;
public class BubbleSort {
    public static void main(String[] args){
        try(Scanner input = new Scanner(System.in)){
            System.out.println("Enter the size of your data list: ");
            int size = input.nextInt();
            System.out.println("Enter your data seperated by spaces: ");
            int[] arr = new int[size];
            for(int i = 0 ; i<arr.length ; i++){
                arr[i] = input.nextInt();
            }
            if(!isSorted(arr)){
                bubbleSort(arr);
                System.out.println("Sorted array: ");
                for(int n : arr){
                    System.out.print(n + " ");
                }
                System.out.println();
            }else{
                System.out.println("Data is sorted.");
            }
        }catch(Exception e){
            System.out.println("Please enter the data as explained.");
        }
    }
    public static void bubbleSort(int[] arr){
        for(int i = 0 ; i<arr.length - 1 ; i++){
            for(int j = 0 ; j<arr.length - 1 - i ; j++){
                if(arr[j] > arr[j + 1]){
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
            System.out.print("Iteration " + i + ": ");
            for(int n : arr){
                System.out.print(n + " ");
            }
            System.out.println();

        }
    }
    public static boolean isSorted(int[] arr){
        for(int i = 0 ; i<arr.length - 1 ; i++){
            if(arr[i] > arr[i + 1]){
                return false;
            }
        }
        return true;
    }
}
