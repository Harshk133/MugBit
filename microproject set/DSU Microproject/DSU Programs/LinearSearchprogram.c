#include<stdio.h>
#include<conio.h>

int main(){
    int arr[10], n, i, key;
    printf("Enter the No. of size for Array: ");
    scanf("%d", &n);

    printf("Enter the Elements in the Array:");
    for(i=0; i<n; i++){
        scanf("%d", &arr[i]);
    }

    printf("Elements in the Array:");
    for(i=0; i<n; i++){
        printf("%d\n", arr[i]);
    }

    printf("Enter the Key Value: ");
    scanf("%d", &key);
    for (i = 0; i < n; i++)
    {
        if(key == arr[i]){
            break;
        }
    }

    if(i == n){
        printf("Element NOt Found !!\n");
    }else{
        printf("%d found at the %dth index in array!\n", key, i+1);
    }    

    return 0;
}