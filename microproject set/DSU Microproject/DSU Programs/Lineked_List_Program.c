#include<stdio.h>
#include<stdlib.h>

struct Node{
    int data;
    struct Node *next;
} *avail;

int main(){
    int n;
    printf("\nLinked List to create and display singly linked list");
    printf("------------------------------------------------\n");
    printf("Input the number of nodes: \n");
    scnaf("%d", &n);


    return 0;
}

void createNodeList(int n){
    struct Node *pre, *temp;
    int num, i;
    avail = (struct Node *) malloc(sizeof(struct Node *));
    if(avail == NULL){
        printf("Memory cannot be allocated");
    }
    else{
        printf("Input data for node one:\n");
        scanf("%d", &num);
        avail -> data = num;
        avail -> next = NULL;
        temp = avail;
        // Creating N Nodes and adding into linked list.
        for(i=2;i<=n;i++){
            pre = (struct Node *) malloc(sizeof(struct Node *));
            if(pre == NULL){
                printf("Memory cannot be allocated!");
                break;
            }
            else{
                printf("Input data for node %d", i);
                scanf("%d", &num);
                pre -> data = num;
                pre -> next = NULL;

                temp -> next = pre;
                temp = temp -> next;
            }
        } 
    }
}

void displayList(){
    struct Node *temp;
    if(avail == NULL){
        printf("List is empty.");
    }
    else{
        temp = avail;
        while(temp!=NULL){
            printf("Data = %d\n", temp->data);
            temp = temp -> next;
        }
    }
}