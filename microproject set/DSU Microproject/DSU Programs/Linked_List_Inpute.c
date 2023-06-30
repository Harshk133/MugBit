#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

struct Node
{
    int data;
    struct Node *next;
};


int main(){
    int i, n;

    // Creating a Node
    struct Node *head = NULL, *ptr = NULL;
    head = malloc(sizeof(struct Node));

    printf("Enter How many types of node you want?\n");
    scanf("%d", &n);
    head -> next = NULL;
    ptr = head;

    printf("Enter the value of First Node/Head:\n");
    scanf("%d", &(head -> data));

    for(i = 1; i <= n; i++){
        struct Node *newNode;

        printf("Enter the value in the %d Node: \n", i);
        scanf("%d", &(newNode -> data));
        head -> next = newNode;
        ptr = ptr -> next = NULL;
    }

    ptr = head;

    while(ptr != NULL){
        printf("Elements are %d", ptr -> data);
        ptr = ptr -> next;
    }

    return 0;
}