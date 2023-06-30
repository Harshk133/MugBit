#include<stdio.h>

int main(){
    int a[5] = {12,34,56,73,11};
    int i, j, temp;
    printf("\nArray Before Sorting:");
    for(i=0; i<5; i++){
        printf("\n%d", a[i]);
    }

    for(i=0; i<4; i++){
        for(j=0; j<4-i; j++){
            if(a[j] > a[j+1]){
                temp = a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
            }
        }
    }

    printf("\nArray After Sorting:");
    for(i=0; i<5; i++){
        printf("\n%d", a[i]);
    }

    return 0;
}