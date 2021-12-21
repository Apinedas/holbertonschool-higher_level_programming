#include "lists.h"

/**
 * check_cycle - looks for a cycle on a single linked list
 * @list: Pointer to list's head
 * Return: 1 if a cycle is found, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *head;

	head = list;
	while (list && list->next)
	{
		if (list->next == head)
			return (1);
	list = list->next;
	}
	return (0);
}
