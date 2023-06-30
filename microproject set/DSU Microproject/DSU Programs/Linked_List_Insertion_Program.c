#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

struct Node{
    int data;
    struct Node *next;
};

void printlist(struct Node *n){
    int c = 0;
    printf("Linked List Elements Are: ");
    while (n != NULL)
    {
        c++;
        printf("\nElments: %d", n -> data);
        n = n -> next;
    }
    printf("\nCount of Node is %d", c);    
}

struct Node * insertAtFirst(struct Node *head, int data){
    struct Node * ptr = (struct Node *) malloc(sizeof(struct Node));
    ptr -> next = head;
    ptr -> data = data;
    return ptr;
}

int main(){
    struct Node *head;
    struct Node *second;
    struct Node *third;
    struct Node *fourth;
    struct Node *fifth;
    struct Node *sixth;

    // Allocating value for the Nodes.
    head = malloc(sizeof(struct Node));
    second = malloc(sizeof(struct Node));
    third = malloc(sizeof(struct Node));
    fourth = malloc(sizeof(struct Node));
    fifth = malloc(sizeof(struct Node));
    sixth = malloc(sizeof(struct Node));

    // Inserting data into it.
    head -> data = 10;
    head -> next = second;

    second -> data = 20;
    second -> next = third;

    third -> data = 30;
    third -> next = fourth;

    fourth -> data = 40;
    fourth -> next = fifth;

    fifth -> data = 50;
    fifth -> next = sixth;

    sixth -> data = 60;
    sixth -> next = NULL;

    printlist(head);
    head = insertAtFirst(head, 70);
    printlist(head);

    return 0;
}