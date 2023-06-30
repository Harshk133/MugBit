#include<stdio.h>

int main(){
    int a[5], i, key;
    printf("Enter 5 elements in array:\n");
    for(i=0; i<5; i++){
        scanf("%d", &a[i]);
    }

    printf("Array contains following elements:\n");
    for(i=0; i<5; i++){
        printf("\n%d", a[i]);
    }
    
    printf("\nEnter the element to search:");
    scanf("%d", &key);

    for(i=0; i<5; i++){
        if(a[i]==key){
            break;
        }
    }
    if(i==5){
        printf("\nElement not found!!");
    }
    else{
        printf("Element is found at %d position", i);
    }

    return 0;
}