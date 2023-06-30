#include<stdio.h>

int main(){
    int top = 0, bottom, a[10], n, i, key, mid;

    printf("Enter 5 elements in array in ascending order:");
    for(i=0; i<5; i++){
        scanf("%d", &a[i]);
    }

    printf("Elements in array\n");
    for(i=0; i<5; i++){
        printf("%d\t", a[i]);
    }

    printf("\nEnter element to search: ");
    scanf("%d", &key);

    mid = (top + bottom)/2;

    while(top<=bottom){
        if(a[mid] == key){
            printf("Element found!");
            break;
        }
        else if(mid > key){
            bottom = mid + 1;
        }
        else{
            top = mid + 1;
            mid = (top + bottom)/2;
        }
        if(top > bottom){
            printf("Element not found!!");
        }
    }

    return 0;
}