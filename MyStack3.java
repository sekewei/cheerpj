import java.util.ArrayDeque;

public class MyStack3 {
    private ArrayDeque<String> stack = new ArrayDeque<>();

    public String push(String item) {
        stack.push(item);
        return "Pushed: " + item;
    }

    public String pop() {
        return stack.isEmpty() ? "Stack empty" : "Popped: " + stack.pop();
    }

    public String peek() {
        return stack.isEmpty() ? "Stack empty" : "Top: " + stack.peek();
    }
}