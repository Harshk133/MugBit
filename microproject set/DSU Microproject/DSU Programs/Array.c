#include<stdio.h>

int main(){
    int n=0, a[n], loc, i;
    printf("Enter how many data you want to store in array:\n");
    scanf("%d", &n);
    printf("Enter YOur Elements:\n");
    for(i=0; i<n; i++){
        scanf("%d", &a[i]);
    }

    printf("Delete Operation:\n");
    printf("Enter the location were you wish to delete element:\n");
    scanf("%d", &loc);
    if(loc>=n+1){
        printf("Deletion is not possible.");
    }
    else{
        for(i=loc-1; i<n; i++){
            a[i]=a[i+1];
        }
    }
    printf("Array after delete operation:\n");
    printf("Array Elements:\n");
    for(i=0; i<n; i++){
        printf("\n%d", a[i]);
    }

    return 0;
}