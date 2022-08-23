#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: singly list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *ls;

	if (list == NULL)
		return (0);
	
	ls = list->next;

	while (ls != NULL)
	{
		if (ls == list)
			return (1);
		ls = ls->next;
	}

	return (0);
}
