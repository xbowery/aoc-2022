import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        File f = new File("input.txt");

        int part1_result = 0;
        int part2_result = 0;

        try (Scanner sc = new Scanner(f)) {
            sc.useDelimiter("\r|\n");
            while (sc.hasNext()) {
                String temp = sc.nextLine();

                String elf1 = temp.split(",")[0];
                String elf2 = temp.split(",")[1];

                int num1_elf1 = Integer.valueOf(elf1.split("-")[0]);
                int num2_elf1 = Integer.valueOf(elf1.split("-")[1]);
                int num1_elf2 = Integer.valueOf(elf2.split("-")[0]);
                int num2_elf2 = Integer.valueOf(elf2.split("-")[1]);

                if ((num1_elf1 <= num1_elf2 && num2_elf1 >= num2_elf2) || (num1_elf1 >= num1_elf2 && num2_elf1 <= num2_elf2)) {
                    part1_result++;
                    part2_result++;
                } else if ((num2_elf1 >= num1_elf2 && num1_elf1 <= num1_elf2) || (num2_elf2 >= num1_elf1 && num1_elf2 <= num1_elf1)) {
                    part2_result++;
                }
            }
        } catch (FileNotFoundException e) {
            System.out.println("File not found.");
        }

        System.out.println("Part 1: " + part1_result);
        System.out.println("Part 2: " + part2_result);
    }
}
