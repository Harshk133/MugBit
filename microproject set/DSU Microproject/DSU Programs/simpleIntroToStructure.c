#include<stdio.h>
#include<string.h>

struct Student
{
    int id;
    int marks;
    char favChar;
    char name[34];
} harsh, harry, om;
// struct Student harsh, harry, om; // global variable

void print(){
    printf("%s\n", harsh.name);
}

int main()
{
    // struct Student harsh, harry, om; // local variable
    // Id for each student
    harsh.id = 1;
    harry.id = 2;
    om.id = 3;

    // Marks for each student
    harsh.marks = 100;
    harry.marks = 99;
    om.marks = 98;

    // Favourite Char for each student
    harsh.favChar = 'H';
    harry.favChar = 'C';
    om.favChar = 'O';

    strcpy(harsh.name, "Harsh Moreshwar Kale");

    // Displaying Date of Student structure memebers.
    // printf("The Name of Student is: %s\n", harsh.name);
    // printf("Harsh got %d marks.\n", harsh.marks);

    // printf("The Name of Student is: %s\n", harsh.name);
    // printf("%s got %d marks.\n",harsh.name, harsh.marks);

    // Calling the function print()
    print();

    return 0;
}
