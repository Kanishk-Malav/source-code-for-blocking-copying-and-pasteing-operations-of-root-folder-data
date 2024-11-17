import java.util.Scanner;
import java.lang.IllegalArgumentException;

public class EMI_calculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the principle amount:");
        double p = sc.nextDouble();

        System.out.println("Enter the annual interest rate(in %):");
        double r = sc.nextDouble() / (12 * 100); // Calculate monthly interest rate

        System.out.println("Enter the loan period:");
        int y = sc.nextInt();

        double emi = calculateEmi(p, r, y);

        System.out.println("EMI: " + emi);

        sc.close();
    }

    public static double calculateEmi(double p, double n, int y) {
        double emi = p * n * Math.pow((1 + n), y) / (Math.pow((1 + n), y) - 1);
        return emi;
    }
}
