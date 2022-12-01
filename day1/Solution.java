import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        String filename = "input.txt";
        File f = new File(filename);

        HashMap<Integer, Integer> map = new HashMap<>();
        int counter = 0;
        int sum = 0;

        try (Scanner scanner = new Scanner(f)) {
            scanner.useDelimiter("\n");
            while (scanner.hasNext()) {
                String temp = scanner.nextLine();
                if (temp.equals("")) {
                    counter += 1;
                    sum = 0;
                } else {
                    sum += Integer.valueOf(temp);
                    map.put(counter, sum);
                }
            }
        } catch (FileNotFoundException e) {
            System.out.println("File not found");
        }

        ArrayList<Integer> values = new ArrayList<>(map.values());
        Collections.sort(values);

        int length = values.size();

        System.out.println("Part 1: " + values.get(length-1));
        System.out.println("Part 2: " + (values.get(length-1) + values.get(length-2) + values.get(length-3)));
    }
}
