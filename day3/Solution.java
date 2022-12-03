import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.Set;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        File f = new File("input.txt");

        part1(f);
        part2(f);
    }

    public static void part1(File f) {
        int sum = 0;
        ArrayList<Character> results = new ArrayList<>();

        try (Scanner sc = new Scanner(f)) {
            sc.useDelimiter("\n|\r");

            while (sc.hasNext()) {
                HashSet<Character> set1 = new HashSet<>();
                HashSet<Character> set2 = new HashSet<>();

                String temp = sc.next();
                String part1 = temp.substring(0, (temp.length() / 2));
                String part2 = temp.substring((temp.length() / 2));

                char[] charArray1 = part1.toCharArray();
                char[] charArray2 = part2.toCharArray();

                for (int i = 0; i < charArray1.length; i++) {
                    set1.add(charArray1[i]);
                    set2.add(charArray2[i]);
                }

                set1.forEach((i) -> {
                    if (set2.contains(i)) {
                        results.add(i);
                    }
                });
            }
        } catch (FileNotFoundException e) {
            System.out.println("File not found.");
        }

        for (Character c : results) {
            sum += getASCIIValue(c);
        }

        System.out.println("Part 1: " + sum);
    }

    public static void part2(File f) {
        int sum = 0;
        ArrayList<Character> results = new ArrayList<>();

        try (Scanner sc = new Scanner(f)) {
            sc.useDelimiter("\n|\r");

            while (sc.hasNext()) {
                char[] charArr1 = sc.nextLine().toCharArray();
                HashSet<Character> set1 = new HashSet<>();
                for (int i = 0; i < charArr1.length; i++) {
                    set1.add(charArr1[i]);
                }

                char[] charArr2 = sc.nextLine().toCharArray();
                HashSet<Character> set2 = new HashSet<>();
                for (int i = 0; i < charArr2.length; i++) {
                    set2.add(charArr2[i]);
                }

                char[] charArr3 = sc.nextLine().toCharArray();
                HashSet<Character> set3 = new HashSet<>();
                for (int i = 0; i < charArr3.length; i++) {
                    set3.add(charArr3[i]);
                }

                set1.forEach(i -> {
                    if (set2.contains(i) && set3.contains(i)) {
                        results.add(i);
                    }
                });
            }
        } catch (FileNotFoundException e) {
            System.out.println("File not found.");
        }

        for (Character c : results) {
            sum += getASCIIValue(c);
        }

        System.out.println("Part 2: " + sum);
    }

    public static int getASCIIValue(Character c) {
        if (c >= 'a' && c <= 'z') {
            return (int) c - 96;
        } else if (c >= 'A' && c <= 'Z') {
            return (int) c - 38;
        } else {
            return -1;
        }
    }
}
