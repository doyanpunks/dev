#include <stdio.h>
#include <stdlib.h>

struct node
{
	int data;
	struct node *next;
};

/* Initialize nodes */
struct node *head;
struct node *one = NULL;
struct node *two = NULL;
struct node *three = NULL;

/* Allocate memory */
one = malloc(sizeof(struct node));
two = malloc(sizeof(struct node));
three = malloc(sizeof(struct node));

/* Assign data values */
one->data = 1;
two->data = 2;
three->data = 3;

/* Connect nodes */ 
one->next = two;
two->next = three;
three->next = NULL;

/* Save address of first node in head */
head = one;

// print the linked list value
void printLinkedList(struct node *p)
{
	while(p != NULL)
	{
		printf("%d ", p->data);
		p = p->next;
	}
}

int main()
{
	// Initialize nodes
	struct node *head;
	struct node *one = NULL;
	struct node *two = NULL;
	struct node *three = NULL;

	// Allocate memory
	one = malloc(sizeof(struct node));
	two = malloc(sizeof(struct node));
	three = malloc(sizeof(struct node));

	// Assigna value values
	one->data = 1;
	two->data = 2;
	three->data = 3;

	// Connect nodes
	one->next = two;
	two->next = three;
	three->next = NULL;

	// printing values
	head = one;
	printLinkedList(head);

	return 0;
}

