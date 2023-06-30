#include<stdio.h>

int main(){
    int arr[10], i, n, temp, k;
    printf("Enter the size of array: ");
    scanf("%d", &n);

    printf("Enter the elements in the array: ");
    for(i=0; i<n; i++){
        scanf("%d", &arr[i]);
    }

    for(i=0; i<n; i++){
        temp = arr[i];
        k = i - 1;
        while((k>=0) && (arr[k] > temp)){
            arr[k+1] = arr[k];
            k = k - 1;
        }
        arr[k+1] = temp;
    }

    printf("Array after sorting: ");
    for(i=0; i<n; i++){
        printf("%d\n", arr[i]);
    }
    return 0;
}