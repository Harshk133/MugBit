#include<stdio.h>
#define size 5

int top = -1, stack[size];

void push();
void pop();
void display();

int main(){
    int choice, i=0;

    while(i>=0){
        printf("_____Stack Operation_____\n");
        printf("1.Push\n2.Pop\n3.Display\n4.Exit\n");
        printf("Enter your choice:\n");
        scanf("%d", &choice);

        switch(choice){
            case 1: push();
            break;

            case 2: pop();
            break;

            case 3: display();
            break;

            case 4: exit(0);
            break;

            default: 
            printf("Enter the correct choice!!");
        }
        i++;
    }


    return 0;
}

void push(){
    int no;
    if(top == size - 1){
        printf("Stack is Full.");
    }
    else{
        printf("Enter the element to insert:\n");
        scanf("%d", &no);
        top = top + 1;
        stack[top] = no;
    }
}

void pop(){
    if(top == -1){
        printf("Stack is empty!!\n");
    }
    else{
        printf("Enter element to pop %d\n", stack[top]);
        top = top - 1;
    }
}

void display(){
    int i;
    if(top == -1){
        printf("Stack is empty!!\n");
    }
    else{
        printf("Elements of Stack: \n");
        for(i=top; i>=0; i--){
            printf("%d", stack[i]);
        }
    }
}

