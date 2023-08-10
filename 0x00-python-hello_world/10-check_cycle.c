#include "lists.h"

/**
 * check_cycle - to check for a singly linked list
 * has a cycle inside
 * @list: pointer to list
 *
 * Tobest_codes
 *
 * Return: 0 if no circle
 *		1 if circle
 */

int check_cycle(listint_t *list)
{
	list = list->next;
	p2 = p2->next->next;

	if (list == p2)
	{
		list = prev;
		prev =  p2;
		while (1)
		{
			p2 = prev;
			while (p2->next != list && p2->next != prev)
			{
				p2 = p2->next;
			}
			if (p2->next == list)
				break;

			list = list->next;
		}
		return (1);
	}
	return (0);
}

