#include <stdio.h>
#include <conio.h>
#include <process.h>
#include <stdlib.h>

typedef struct node
{
    /* data */
    int data;
    struct node *next;
} node;
node *p, *head;

int i, num, n;

int main()
{

    printf("\n Enter the no. of nodes : ");
    scanf("%d", &n);

    head = (node*)malloc(sizeof(node));
    head->next = NULL;
    printf("\n Enter the data of head");
    scanf("%d", &head->data);
    p = head;
    for (i = 1; i < n; i++)
    {
        /* code */
        p->next = (node*)malloc(sizeof(node));

        p=p->next;

        printf("Enter the data : ");
        scanf("%d", &(p->data));
        
        p->next = NULL;
    }

    p = head;

    while (p != NULL)
    {
        /* code */
        printf("%d->", p->data);
        p = p->next;
    }

    return 0;
}