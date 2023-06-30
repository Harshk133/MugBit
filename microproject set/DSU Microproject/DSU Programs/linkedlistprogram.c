#include<stdio.h>
#include<stdlib.h>

struct Node {
    int data;
    struct Node * next;
};

void printList(struct Node *n){
    int count;
    printf("Linked list elements are:");
    while(n != NULL){
        count++;
        printf("\n%d", n->data);
        n = n -> next;
    }
    printf("\nNumber of Nodes are %d", count);
}

int main(){
    // Declaring each node.
    struct Node * head;
    struct Node *  second;
    struct Node *  third;

    // Assigning the size for each node.
    head = (struct Node *) malloc(sizeof(struct Node));
    second = (struct Node *) malloc(sizeof(struct Node));
    third = (struct Node *) malloc(sizeof(struct Node));

    // link to head
    head -> data = 10;
    head -> next = second;

    // link to second
    second -> data = 20;
    second -> next = third;

    // link to third
    third -> data = 30;
    third -> next = NULL;

    // Calling the function
    printList(head);

    return 0;
}