import java.util.ArrayDeque;
import java.util.Deque;

public class MyStack {
    private final Deque<String> stack = new ArrayDeque<>();

    public String push(String value) {
        stack.push(value);
        return contents();
    }

    public String pop() {
        return stack.isEmpty() ? "The stack is empty." : stack.pop();
    }

    public String peek() {
        return stack.isEmpty() ? "The stack is empty." : stack.peek();
    }

    public String contents() {
        return stack.toString();
    }

    // Exports the current stack as a list-style string for JavaScript.
    public String export() {
        return contents();
    }

    public static void main(String[] args) {
        MyStack demo = new MyStack();
        demo.push("A");
        demo.push("B");
        demo.push("C");
        System.out.println("Stack after push: " + demo.contents());
        System.out.println("Peek: " + demo.peek());
        System.out.println("Pop: " + demo.pop());
        System.out.println("Stack after pop: " + demo.contents());
    }
}
