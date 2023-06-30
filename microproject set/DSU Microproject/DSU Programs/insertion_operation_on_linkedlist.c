#include<stdio.h>
#include<malloc.h>

struct Node {
    int data;
    struct Node *next;
};

void printList(struct Node *ptr){
    int c = 0;
    printf("LinkedList Elements:");
    while (ptr != NULL)
    {
        c++;
        printf("\n%d", ptr->data);
        ptr = ptr-> next;
    }
    printf("\nNumber of node %d", c);
    
}

// Insert at first..
struct Node * insertAtFirst(struct Node *head, int data){
    struct Node *ptr;
    ptr = malloc(sizeof(struct Node));
    ptr -> next = head;
    ptr -> data = data;
    return ptr;
}

// Insert at Index position..
struct Node * insertAtIndex(struct Node *head, int data, int index){
    struct Node *ptr = malloc(sizeof(struct Node));
    struct Node *p = head;
    int i = 0;

    while(i != index - 1){
        p = p -> next;
        i++;
    }
    ptr -> data = data;
    ptr -> next = p -> next;
    p -> next = ptr;

    return head;
}

// Insert at End..
struct Node * insertAtEnd(struct Node *head, int data){
    struct Node *ptr = malloc(sizeof(struct Node));
    ptr -> data = data;
    struct Node *p = head;

    while(p->next != NULL){
        p = p -> next;
    }
    p->next = ptr;
    ptr->next = NULL;
    return head;
}

struct Node * insertAfterNode(struct Node *head, struct Node *prevNode, int data){
    struct Node *ptr = malloc(sizeof(struct Node));
    ptr->data = data;

    ptr->next=prevNode->next;
    prevNode->next=ptr;

    return head;
}

int main(){
    // Declaring Nodes
    struct Node *head;
    struct Node *second;
    struct Node *third;
    struct Node *fourth;

    // Assigning the memory allocation for each node
    head = malloc(sizeof(struct Node));
    second = malloc(sizeof(struct Node));
    third = malloc(sizeof(struct Node));
    fourth = malloc(sizeof(struct Node));

    // Assigning the value in data and linked it to the node.
    head -> data = 10;
    head -> next = second;

    // Assigning the value in data and linked it to the node.
    second -> data = 20;
    second -> next = third;
    
    // Assigning the value in data and linked it to the node.
    third -> data = 30;
    third -> next = fourth;
    
    // Assigning the value in data and linked it to the node.
    fourth -> data = 40;
    fourth -> next = NULL;

    // Calling the function
    // printList(second);

    // Calling the function
    // head = insertAtFirst(head, 50);
    // head = insertAtIndex(head, 22, 1);
    // head = insertAtEnd(head, 01);
    head = insertAfterNode(head, third, 01);
    printList(head);

    return 0;
}