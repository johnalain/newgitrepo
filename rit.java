
class Car{
    String type;
    int price;
    int speed;

void setName(String n){
    type = n;
}

String getName(){
    return type;
}}
class Main{
    public static void main(String[] args) {
        Car ob = new Car();
        ob.type = "honda";
        ob. setName("mercedes");
        System.out.println(ob.getName());
        //https://youtu.be/JIPwPCkYoLY?list=PLlvFEn0NKwXI94-MnWtV4oifwwEvy6uN3&t=902
        // Car ob; //declare object car
        // ob = new Car();//booked memory location
        // Car ob1 = new Car();
        
        // System.out.println(ob.type);
        // System.out.println(ob.price);
        // System.out.println(ob.speed);
        // ob1.type="mercedes";
        // ob1.price = 12000;
        // ob1.speed =240;
        // System.out.println(ob1.type);
        // System.out.println(ob1.price);
        // System.out.println(ob1.speed);

    }
}