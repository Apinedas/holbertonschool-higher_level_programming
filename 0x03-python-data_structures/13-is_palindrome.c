#include "lists.h"

/**
 * add_nodeint - adds a new node at the head of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = *head;

	*head = new;

	return (new);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *reversed, *current, *current_rev;

	current = *head;
	reversed = NULL;
	while (current)
	{
		add_nodeint(&reversed, current->n);
		current = current->next;
	}
	current = *head;
	current_rev = reversed;
	while (current && current_rev)
	{
		if (current->n == (current_rev)->n)
		{
			current = current->next;
			current_rev = (current_rev)->next;
		}
		else
		{
			free_listint(reversed);
			return (0);
		}
	}
	free_listint(reversed);
	return (1);
}
