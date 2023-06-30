// Including Header files
#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
// Defining size variable globally
#define size 10

// Initializing some variables important for Queue.
int front = -1, rear = -1;
int queue[size];

// Prototyping of functions
int insert();
int delete();
int display();

// Entry point of the programing i.e. int main function.
int main(){
    int choice, i;
    printf("_________Queue_Operation_________\n");
    printf("1.Insert\n2.Delete\n3.Display\n4.Exit\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    while (i>=0)
    {
        switch(choice){
            case 1: insert();
            break;

            case 2: delete();
            break;

            case 3: display();
            break;

            case 4: exit(0);
            break;

            default:
                printf("Please, Enter the Valid Choice!!");
        }
        i++;
    }
    

    return 0;
}

// Defining the functions
int insert(){
    int no;
    if(rear == size - 1){
        printf("Queue is Full, Hence Overflow condition met..\n");
    }else if(front == -1){
        front = 0;
    }else{
        printf("Enter the Number for Inserting it to the Queue: \n");
        scanf("%d", &no);
        rear = rear + 1;
        queue[rear] = no;
    }
}

// Defining the functions
int delete(){
    if(front == -1){
        printf("Queue is Empty, Hence Underflow condition met..\n");
    }else{
        printf("Element is deleted %d from the Queue! \n", queue[front]);
        front = front - 1;
        if(front > rear)
            front = rear = -1;
    }
}

// Defining the functions
int display(){
    int i;
    if(front == -1){
        printf("Stack is Empty!\n");
    }else{
        printf("The Elements of Queue is:\n");
        for(i = front; i <= rear; i++){
            printf("%d\n", queue[i]);
        }
    }
}
