#include<stdio.h>
#define size 5

int top = -1, stack[size];

void push();
void pop();
void display();
void exit();

void main(){
    int choice, i=0;
    while (i>=0)
    {
        printf("\n_____Stack Operations_____\n");
        printf("\n1.PUSH\n2.POP\n3.DISPLAY\n4.EXIT\n");
        printf("\nEnter YOur Choice:\n");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            push();
            break;

        case 2:
            pop();
            break;
        case 3:
            display();
            break;

        case 4:
            exit(0);
            break;
        
        default:
            printf("\nEnter the correct choice!!\n");
            break;
        }
        i++;
    }
    
}

void push(){
    int no;
    if(top == size - 1){
        printf("\nStack is full!!\n");
    }
    else{
        printf("Enter the number to push: \n");
        scanf("%d", &no);
        top = top + 1;
        stack[top] = no;
    }
}

void pop(){
    if(top == -1){
        printf("\nStack is empty!!\n");
    }
    else{
        printf("Deleted element is %d : ", stack[top]);
        top = top - 1;
    }
}

void display(){
    int i;
    if(top == -1){
        printf("Stack is empty!!");
    }
    else{
        printf("Stack:\n");
        for(i=top;i>=0;i--){
            printf("\n%d", stack[i]);
        }
    }
}