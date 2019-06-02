import java.util.Scanner;

class InsertionSort {
    static void sort(int[] arr) {
	for (int i = 1; i < arr.length; i++) {
	    int j = i;
	    while ((j > 0) && (arr[j] < arr[j - 1])) {
		int temp = arr[j];
		arr[j] = arr[j - 1];
		arr[j - 1] = temp;
		j--;
	    }
	}
    }
    
    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);

	System.out.println("Enter the count of numbers");
	int n = scanner.nextInt();
	int[] arr = new int[n];
	
	System.out.println("Enter the numbers to sort");
	for (int i = 0; i < n; i++) {
	    arr[i] = scanner.nextInt();
	}
	sort(arr);

	for (int i = 0; i < n; i++) {
	    System.out.print(arr[i] + " ");
	}
	System.out.println();
    }
}
