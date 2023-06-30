#include<stdio.h>
#define size 10

int front = -1, rear = -1;
int queue[size];

void insert();
void delete();
void display();

int main(){
    int choice, i = 0;
    while(i>=0){
        printf("____Queue Operations____\n");
        printf("1.Insert\n2.Delete\n3.Display\n4.Exti");

        printf("\nEnter your choice:");
        scanf("%d", &choice);

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
            printf("Enter a Valid choice!!");
        }
        i++;
    }


    return 0;
}

void insert(){
    int no;
    if(rear == size - 1){
        printf("Queue is Full!!");
    }
    else if(front == - 1){
        front = 0;
    }
    else{
        printf("Enter Numbr to be inserted:\n");
        scanf("%d", &no);
        rear = rear + 1; 
        queue[rear] = no;
    }
}

void delete(){
    if(front == -1){
        printf("Queue is Empty!!");
    }
    else{
        printf("Deteleted element %d", queue[front]);
        front = front - 1;
        if(front > rear)
            front = rear = -1;
    }
}

void display(){
    int i;
    if(front == -1){
        printf("Queue is Empty!");
    }
    else{
        for(i = front; i <= rear; i++){
            printf("%d", queue[i]);
        }
    }
}