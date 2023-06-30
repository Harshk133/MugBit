#include<stdio.h>

typedef struct Student{
    int id;
    int marks;
    char favChar;
    char name[30];
} std;

int main()
{
    // struct Student s1, s2;
    std s1, s2;
    s1.id = 1;
    s2.id = 2;
    printf("Value of s1's Id is %d\n", s1.id);
    printf("Value of s2's Id is %d\n", s2.id);
    // typedef <previous name> <alias name>
    // typedef unsigned long ul;
    // ul l1, l2, l3;
    return 0;
}
