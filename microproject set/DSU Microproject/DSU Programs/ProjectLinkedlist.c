#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<string.h>

struct Node{
    char name[20];
    struct Node *next;
};
// struct Node{
//     char data;
//     struct Node *next;
// };

void printlist(struct Node *n){
    int c = 0;
    printf("Elements of Linked lists: \n");
    while(n != NULL){
        c++;
        printf("\t%d", n -> name);
        n = n -> next;
    }
    printf("The Number of Nodes are %d", c);
}

int main(){
    struct Node *node = NULL;
    node = malloc(sizeof(struct Node));

    // node -> name = "Harsh";
    strcpy(node->name, name);
    node -> next = NULL;

    printlist(node);



    return 0;
}