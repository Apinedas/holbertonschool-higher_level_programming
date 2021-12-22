#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: pointer to list's head node
 * @number: numer to add
 * Return: Adress of the new node, or NULL in failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ret, *actual_node;

	if (!*head)
		return (NULL);
	ret = malloc(sizeof(*ret));
	if (ret == NULL)
		return (NULL);
	ret->n = number;
	actual_node = *head;
	while (actual_node)
	{
		if (number < actual_node->n && actual_node == *head)
		{
			ret->next = actual_node;
			*head = ret;
			return (ret);
		}
		else if (actual_node->next && (number < actual_node->next->n))
		{
			ret->next = actual_node->next;
			actual_node->next = ret;
			return (ret);
		}
		else if (number > actual_node->n && actual_node->next == NULL)
		{
			actual_node->next = ret;
			ret->next =  NULL;
			return (ret);
		}
		actual_node = actual_node->next;
	}
	free(ret);
	return (NULL);
}
