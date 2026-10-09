package tamgiac;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner inp = new Scanner(System.in);
        int t = inp.nextInt();
        while(t-- > 0){
            Point [] d = new Point[3];
            for(int i = 0; i < 3;i++){
                double x = inp.nextDouble();
                double y = inp.nextDouble();
                d[i] = new Point(x, y);
            }
            double a = d[0].distance(d[1]);
            double b = d[1].distance(d[2]);
            double c = d[0].distance(d[2]);
            if(a + b > c && b + c > a && a + c > b){
                System.out.printf("%.3f\n", a + b + c);
            } else{
                System.out.println("INVALID");
            }
        }
        inp.close();
    }
}
