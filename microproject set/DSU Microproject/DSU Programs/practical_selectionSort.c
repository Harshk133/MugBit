#include<stdio.h>

int main(){
    int a[5] = {45, 12, 30, 67, 39};
    int i, j, temp;

    printf("\nArray Before Sorting:");
    for(i=0; i<5; i++){
        printf("%d\t", a[i]);
    }

    for(i=0; i<5; i++){
        for(j=i+1; j<5; j++){
            if(a[i] > a[j]){
                temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
    }

    printf("\nArray After Sorting:");
    for(i=0; i<5; i++){
        printf("%d\t", a[i]);
    }

    return 0;
}