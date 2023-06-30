// C Program to insert an element in a linear queue using array.
#include<stdio.h>
#include<conio.h>
#define n 5

int main(){
    int queue[n], ch = 1, front = 0, rear = 0, i, j, x = n; 
    printf("Queue Using Array");
    printf("\n1.Insertion\n2.Display\n3.Exit");
    while(ch){
        printf("Enter the choice: ");
        scanf("%d", &ch);
        switch (ch)
        {
        case 1:
            if(rear==x){
                printf("\nQueue is Full");
            }
            else{
                printf("\nEnter no %d:", j++);
                scanf("%d", &queue[rear++]);
            }
            break;

        case 2:
            printf("\nQueue Element are:\n");
            if(front==rear){
                printf("Queue is Empty");
            }
            else{
                for(i=front; i<rear; i++){
                    printf("%d", queue[i]);
                    printf("\n");
                }
            }
            break;
        
        case 3:
            exit(0);
        
        default:
            printf("Wrong Choice, please see the options");
        }
    }

    getch();
    return 0;
}