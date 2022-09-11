package ds;

public class SinglyLinkedList {
    Node headNode;
    Node tailNode;

    public SinglyLinkedList(Node head){
        this.headNode = head;
        this.tailNode = null;
    }

    public void traverse() {
        // Traverse once through the LL and print each nodes' value.
        Node currentNode = this.headNode;
        while(true){
            System.out.println(currentNode.value);
            if (currentNode.nextNode == null){
                this.tailNode = currentNode;
                break;
            }
            currentNode = currentNode.nextNode;
        }
    }
    
    public void append(Node node){
        // Append Node to LL
        Node currentNode = this.headNode;
        if (this.tailNode != null){
            currentNode = this.tailNode;
        }
        while (currentNode.nextNode != null){
            currentNode = currentNode.nextNode;
        }
        currentNode.nextNode = node;
        System.out.println("Appended node to Linked List.");
    }

    public static void main(String[] args) {
        Node head = new Node(0);
        Node n1 = new Node(1);
        Node n2 = new Node(2);
        Node n3 = new Node(3);
        SinglyLinkedList sll = new SinglyLinkedList(head);
        sll.append(n1);
        sll.append(n2);
        sll.append(n3);

        sll.traverse();
    }
}
