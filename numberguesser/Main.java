import java.util.Random;
import java.util.Scanner;

class Main{
    static Scanner s = new Scanner(System.in);
    static Random random = new Random();
    static int x=0;
    static int limit=15;
    static int max=100;
    public static void displaymenu(){
            int diff=0; 
            boolean p=false; 
                do{
                System.out.println("_____________________________________________________");
                System.out.println("Enter the level of difficulty:\n1. Easy(1-50)\n2. Medium(1-100)\n3. Hard(1-200)");
                System.out.println("Enter the choice:");
                while(!s.hasNextInt()){
                    
                   System.out.println("INVALID INPUT !!!\nEnter the number again");
                    s.next();
                }
                diff=s.nextInt();
                switch (diff) {
                    case 1:
                        x=random.nextInt(50)+1;  
                        limit=15;
                        max=50; 
                        p=false;
                        break;
                    case 2:
                        x=random.nextInt(100)+1; 
                        limit=10;
                        max=100;
                        p=false;
                        break;
                    case 3:
                        x=random.nextInt(200)+1;
                        limit=5;
                        max=200;
                        p=false;
                        break;  
                    default:
                        System.out.println("Invalid difficulty!!");
                        p=true;
                        break;
                }
            }while(p);
    }
    public static boolean numberGuesser(){
        try{
            int num;
            int c=0;
            do
            {
                System.out.println("Guess the number: ");
                while(!s.hasNextInt()){
                   System.out.println("INVALID INPUT !!!\nEnter the number again");
                    s.next();
                }
                num=s.nextInt();
                if(num>max || num<1)
                {
                    System.out.println("Out of range");
                    continue;
                }
                c++;
                if(num>x)
                    System.out.println("Too High");
                else if(num<x)
                    System.out.println("Too low");
                else{
                    System.out.println("Correct answer ,the total number of guess is "+c);
                    break;
                }
                System.out.println("remaining chances:"+(limit-c));
                if(c>=limit)
                {
                    System.out.println("Sorry your out of chances");
                    break;
                }  
            }while(x!=num);
        }catch(Exception E)
        {
            System.out.println(" "+E.getMessage());
        }
        String opt;
        System.out.println("_____________________________________________________");
        System.out.println("Do you want to play again:Y/N");
        opt=s.next(); 
        if(opt.equalsIgnoreCase("Y"))   
            return true;
        else    
            return false;
        
    }
    public static void main(String[] args) {
        boolean option;
        do{
            displaymenu();
            option=numberGuesser();          
        }while(option);
    }
}