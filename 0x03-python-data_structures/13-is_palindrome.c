#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
    listint_t *current, *compare;
	int list_lenght = 0, movements = 0, moved = 0;

    if (head)
    {
        current = *head;
        while (current)
        {
            list_lenght++;
            current = current->next;
        }
        movements = list_lenght - 1;
        current = *head;
        while (movements > 0)
        {
            compare = current;
            while(moved != movements)
            {
                compare = compare->next;
                moved++;
            }
            if (current->n == compare->n)
            {
                current = current->next;
                movements -= 2;
                moved = 0;
            }
            else
                return (0);
        }
        return (1);
}
