import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Solution {
    public static HashMap<String, Map<String, Integer>> part1_scoreboard = new HashMap<>();
    public static HashMap<String, Map<String, Integer>> part2_scoreboard = new HashMap<>();

    public static void initialise_part1_scoreboard(HashMap<String, Map<String, Integer>> part1_scoreboard) {
        part1_scoreboard.put("A", Map.of("X", 4, "Y", 8, "Z", 3));
        part1_scoreboard.put("B", Map.of("X", 1, "Y", 5, "Z", 9));
        part1_scoreboard.put("C", Map.of("X", 7, "Y", 2, "Z", 6));
    }

    public static void initialise_part2_scoreboard(HashMap<String, Map<String, Integer>> part2_scoreboard) {
        part2_scoreboard.put("A", Map.of("X", 3, "Y", 4, "Z", 8));
        part2_scoreboard.put("B", Map.of("X", 1, "Y", 5, "Z", 9));
        part2_scoreboard.put("C", Map.of("X", 2, "Y", 6, "Z", 7));
    }

    public static Integer sum_part1_score(String opponent_choice, String my_choice) {
        return part1_scoreboard.get(opponent_choice).get(my_choice);
    }

    public static Integer sum_part2_score(String opponent_choice, String my_choice) {
        return part2_scoreboard.get(opponent_choice).get(my_choice);
    }

    public static void main(String[] args) {
        initialise_part1_scoreboard(part1_scoreboard);
        initialise_part2_scoreboard(part2_scoreboard);

        File f = new File("input.txt");
        int part1_score = 0;
        int part2_score = 0;

        try (Scanner sc = new Scanner(f)) {
            sc.useDelimiter("\n|\r");

            while(sc.hasNext()) {
                String temp = sc.nextLine();

                String opponent_choice = temp.split(" ")[0];
                String my_choice = temp.split(" ")[1];

                part1_score += sum_part1_score(opponent_choice, my_choice);
                part2_score += sum_part2_score(opponent_choice, my_choice);
            }
        } catch (FileNotFoundException e) {
            System.out.println("File not found!");
        }

        System.out.println("Part 1: " + part1_score);
        System.out.println("Part 2: " + part2_score);
    }
}
