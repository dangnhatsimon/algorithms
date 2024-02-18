/* *****************************************************************************
 *  Name:              Ada Lovelace
 *  Coursera User ID:  123456
 *  Last modified:     October 16, 1842
 **************************************************************************** */

import edu.princeton.cs.algs4.StdOut;

public class HelloGoodbye {
    public static void main(String[] args) {
        String first = args[0];
        String second = args[1];
        StdOut.println("Hello " + first + " and " + second + ".");
        StdOut.println("Goodbye " + second + " and " + first + ".");
    }
}
