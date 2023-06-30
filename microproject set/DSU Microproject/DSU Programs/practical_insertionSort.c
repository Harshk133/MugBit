#include<stdio.h>

int main(){
    int a[5] = {12, 32, 10, 56, 75};
    int i, j, k, temp;
    
    printf("Array Before Sorting:\n");
    for(i=0; i<5; i++){
        printf("%d\t", a[i]);
    }

    for(i=1; i<5; i++){
        temp = a[i];
        k = i - 1;
        while((k>=0) && (a[k] > temp)){
            a[k+1] = a[k];
            k = k - 1;
        }
        a[k+1] = temp;
    }

    printf("\nArray After Sorting:\n");
    for(i=0; i<5; i++){
        printf("%d\t", a[i]);
    }
    return 0;
}