import java.io.*;
import java.util.*;

public class Solution {
    
    public static void main(String[] args) {
        File f = new File("input.txt");

        Map<String, Long> directorySize = new HashMap<>();
        Deque<String> directoryList = new ArrayDeque<>();

        try (Scanner sc = new Scanner(f)) {
            sc.useDelimiter("\n|\r");
            while (sc.hasNext()) {
                String line = sc.nextLine();

                String[] lineArr = line.split(" ");

                if ((lineArr[0].equals("$")) && (lineArr[1].equals("cd"))) {
                    if (lineArr[2].equals("/")) {
                        directoryList.add("");
                    } else if (lineArr[2].equals("..")) {
                        directoryList.removeLast();
                    } else {
                        String previousDir = directoryList.peekLast();
                        directoryList.addLast(previousDir + "/" + lineArr[2]);
                    }
                } else if ((lineArr[0].equals("dir")) || (lineArr[0].equals("$") && lineArr[1].equals("ls"))) {
                    continue;
                } else {
                    for (String s : directoryList) {
                        directorySize.merge(s, Long.valueOf(lineArr[0]), Long::sum);
                    }
                }
            }
        } catch (FileNotFoundException e) {
            System.out.println("File not found.");
        }

        System.out.println("Part 1: " + part1(directorySize));
        System.out.println("Part 2: " + part2(directorySize));
    }


    static long part1(Map<String, Long> directorySize) {
        final int TOTAL_SIZE = 100000;

        long result = 0;

        List<Long> values = new ArrayList<>(directorySize.values());

        for (Long v : values) {
            if (v <= TOTAL_SIZE) {
                result += v;
            }
        }

        return result;
    }

    static long part2(Map<String, Long> directorySize) {
        final int REQUIRED_SIZE = 30000000;
        final int TOTAL_SIZE = 70000000;

        long result = 30000000;

        long unusedSize = TOTAL_SIZE - directorySize.get("");
        long sizeToClear = REQUIRED_SIZE - unusedSize;

        if (sizeToClear <= 0) {
            return 0;
        }

        List<Long> values = new ArrayList<>(directorySize.values());

        for (Long v : values) {
            if ((v >= sizeToClear) && (v < result)) {
                result = v;
            }
        }

        return result;
    }
}
