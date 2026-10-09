package tamgiac;
import static java.lang.Math.sqrt;
import static java.lang.Math.pow;

public class Point{
    private double x;
    private double y;
    public Point(){
        this(0.0, 0.0);
    }
    public Point(double x, double y){
        this.x = x;
        this.y = y;
    }
    public Point(Point p){
        this.x = p.x;
        this.y = p.y;
    }
    public double getX(){
        return x;
    }
    public double getY(){
        return y;
    }
    public double distance(Point p){
        return sqrt(pow(this.x - p.x, 2) + pow(this.y - p.y, 2));
    }
    public static double distance(Point a, Point b){
        return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2));
    }
    @Override
    public String toString(){
        return x + " " + y;
    }
}
