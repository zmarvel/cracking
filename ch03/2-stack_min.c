#include <stdio.h>
#include <stdlib.h>

struct node{
  int data;
  int min;
  struct node* next;
};

struct stack{
  struct node* head;
};

struct node* new_node(int data, int min){
  struct node* newNode = (struct node*)malloc(sizeof(struct node));

  newNode->data = data;
  newNode->min = min;
  newNode->next = NULL;
}

void push(struct stack* s, int data){
  struct node* newNode;
  if (s->head == NULL){
    newNode = new_node(data, data); //question mark operator
  }
  else{
    newNode = new_node(data, (min(s) > data) ? data:min(s)); //question mark operator
  }
  newNode->next = s->head;
  s->head = newNode;
}

void pop(struct stack* s){
  s->head = s->head->next;
}

int min(struct stack* s){
  return s->head->min;
}


void main(){
struct stack* s = (struct stack*)malloc(sizeof(struct stack));
 s->head = NULL;
 push(s, 9);
 push(s, 7);
 push(s, 5);
 push(s, 3);
 push(s, 1);


 printf("current min: %i \n", min(s));
 pop(s);

 printf("current min: %i \n", min(s));
 pop(s);

 printf("current min: %i \n", min(s));
 pop(s);

 printf("current min: %i \n", min(s));
 pop(s);

}
