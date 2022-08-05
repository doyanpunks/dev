//define a doubly linked list of heap-allocated strings. Write functions to insert, find, and delete items from it. Test them.

#include "stdio.h"
#include <stdlib.h>

struct Node 
{
   int* prev;
   int* next;
   const char* data;
};

// insert node at the front
void insertFront(struct Node** head, char* data)
{
   // allocate mem for newNode
   struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));

   // assign data to newNode
   newNode->data = data;

   // make newNode as a head
   newNode->next = (*head);

   // assign null to prev
   newNode->prev = NULL;

   // previous of head (now head is the second node) is newNode
   if((*head) != NULL)
   {
      (*head)->prev = newNode;
   }

   // head points to newNode
   (*head) = newNode;
}

// insert a node after a specific node
void insertAfter(struct Node* prev_node, char* data)
{
   if(prev_node == NULL)
   {
      printf("previous node cannot be null");
   }
   return;

   // allocate mem for newNode
   struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));

   // assign data to newNode
   newNode->data = data;

   // set next of newNode to next of prev node
   newNode->next = prev_node->next;

   // set next of prev node to newNode
   newNode->prev = prev_node;

   // set prev of newNode's next to newNode
   if(newNode->next != NULL)
   {
      newNode->next->prev = newNode;
   }
}

// insert a newNode at the end of the list
void insertEnd(struct Node** head, char* data)
{
   // allocate mem for node
   struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));

   // assign data to newNode
   newNode->
}



























