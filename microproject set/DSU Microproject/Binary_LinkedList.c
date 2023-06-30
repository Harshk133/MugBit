#include<stdio.h>
#include<malloc.h>

struct Node{
    int data;
    struct node *left;
    struct node *right;
};

struct Node* createNode(int data){
    p = (struct Node *) malloc(sizeof(struct Node));
    p -> data =2;
    p -> left = NULL;
    p -> right = NULL;
}

int main(){
    struct Node *p;
    p = (struct Node *) malloc(sizeof(struct Node));
    p -> data =2;
    p -> left = NULL;
    p -> right = NULL;

    struct Node *p1;
    p1 = (struct Node *) malloc(sizeof(struct Node));
    p -> data = 1;
    p1 -> left = NULL;
    p1 -> right = NULL;

    struct Node *p2;
    p2 = (struct Node *) malloc(sizeof(struct Node));
    p -> data = 4;
    p2 -> left = NULL;
    p2 -> right = NULL;

    p -> left = p1;
    p -> right = p2;

    return 0;
}