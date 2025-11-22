import java.util.Random;
import java.util.Scanner;

class Main{
    static Scanner s = new Scanner(System.in);
    public static boolean numberGuesser(){
        try{
            Random random = new Random();
            int x=random.nextInt(100)+1;  
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
                if(num>100 || num<1)
                {
                    System.out.println("Out of range!");
                    break;
                }
                if(num>x)
                    System.out.println("Too High");
                else if(num<x)
                    System.out.println("Too low");
                else
                    System.out.println("Correct answer ,the total number of guess is "+c);
                c++;
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
            option=numberGuesser();          
        }while(option);
    }
}