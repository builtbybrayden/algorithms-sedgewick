//Write a program that takes three integer command line arguments and prints equal if all three are equal, and not equal otherwise

public class threeEqualInts
{
    public static String comparison(int[] numbers)
    {
        if (numbers[0] == numbers[1] && numbers[1] == numbers[2]) 
        {
            return "Equal";
        }
        else 
        {
            return "Not Equal";
        }
    }

    public static void main(String[] args)
    {
        if (args.length != 3)
        {
            System.err.println("Usage: java threeEqualInts <int> <int> <int>");
            return;
        }

        int[] numbers = new int[3];
        for (int i = 0; i < numbers.length; i++)
        {
            numbers[i] = Integer.parseInt(args[i]);
        }

        String result = comparison(numbers);
        System.out.println(result);
    }
}