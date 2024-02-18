/* *****************************************************************************
 *  Name:              Ada Lovelace
 *  Coursera User ID:  123456
 *  Last modified:     October 16, 1842
 **************************************************************************** */

import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class RandomWord {
    public static void main(String[] args) {
        double index = 1.0;
        String champion = "";
        while (!StdIn.isEmpty()) {
            String word = StdIn.readString();
            boolean valid = StdRandom.bernoulli(1.0 / index);
            if (valid) {
                champion = word;
            }
            index++;
        }
        StdOut.println(champion);

    }
}
