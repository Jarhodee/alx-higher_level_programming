#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @v: integer
 * @nextd: points to the next node
 * Description: singly linked list node structure
 * for Holberton project
 * */

typedef struct listint_s
{
	int v;
	struct listint_s *nextd;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int v);
void free_listint(listint_t *head);
int is_palindrome(listint_t **head);

#endif
