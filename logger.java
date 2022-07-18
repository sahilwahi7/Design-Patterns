import java.util.*;

public class MyLogger implements Logger {
    private Map<String, Long> startMap = new HashMap<>();
    private PriorityQueue<Node> minHeap = new PriorityQueue<>((node1, node2) -> Long.compare(node1.start, node2.start));

    /**
     * When a process starts, it calls 'start' with processId and startTime.
     */
    @Override
    public void start(String processId, long startTime) {
        startMap.put(processId, startTime);
    }

    /**
     * When the same process ends, it calls 'end' with processId and endTime.
     */
    @Override
    public void end(String processId, long endTime) {
        if (!startMap.containsKey(processId)) {
            throw new IllegalArgumentException("cannot end a process which has not been started, process not found");
        }

        Node process = new Node(processId, startMap.get(processId), endTime);

        // clean up hashmap
        startMap.remove(processId);

        minHeap.offer(process);
    }

    /**
     * Prints the logs of this system sorted by the start time of processes in the below format
     * {processId} started at {startTime} and ended at {endTime}
     */
    @Override
    public void print() {
        while (!minHeap.isEmpty()) {
            Node process = minHeap.poll();

            System.out.println(process.pid + " started at " + process.start + " and ended at " + process.end);
        }
    }

    private class Node {
        String pid;
        Long start;
        Long end;

        Node(String pid, long start, long end) {
            this.pid = pid;
            this.start = start;
            this.end = end;
        }
    }

    public static void main(String[] args) {
        /*
        Output:
            1 started at 100 and ended at 104
            2 started at 101 and ended at 102
            3 started at 103 and ended at 105
         */

        Logger log = new MyLogger();
        log.start("1", 100);
        log.start("2", 101);
        log.end("2", 102);
        log.start("3", 103);
        log.end("1", 104);
        log.end("3", 105);
        log.print();

    }
}
