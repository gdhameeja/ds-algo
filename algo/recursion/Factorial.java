import java.util.Scanner;

class Factorial{
  static int fact(int n){
    if(n==1){
      return 1;
    }
    return n * fact(n-1);
  }

  public static void main(String[] args){
    Scanner scanner = new Scanner(System.in);
    assert fact(5) == 120;
    System.out.println(fact(5));
  }
}
