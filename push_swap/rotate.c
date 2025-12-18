/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rotate.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ndebavel <ndebavel@student.42lehavre.fr>   +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/24 11:58:06 by ndebavel          #+#    #+#             */
/*   Updated: 2025/12/15 13:27:59 by ndebavel         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ra(t_stack **a)
{
	t_stack	*temp;
	t_stack	*last;

	if (!a || !*a || !(*a)->next)
		return ;
	temp = *a;
	*a = (*a)->next;
	temp->next = NULL;
	last = *a;
	while (last->next)
		last = last->next;
	last->next = temp;
	write(1, "ra\n", 3);
}

void	rb(t_stack **b)
{
	t_stack	*temp;
	t_stack	*last;

	if (!b || !*b || !(*b)->next)
		return ;
	temp = *b;
	*b = (*b)->next;
	temp->next = NULL;
	last = *b;
	while (last->next)
		last = last->next;
	last->next = temp;
	write(1, "rb\n", 3);
}

void	rr(t_stack **a, t_stack **b)
{
	t_stack	*temp;
	t_stack	*last;

	if (!b || !*b || !(*b)->next)
		return ;
	if (!a || !*a || !(*a)->next)
		return ;
	temp = *a;
	*a = (*a)->next;
	temp->next = NULL;
	last = *a;
	while (last->next)
		last = last->next;
	last->next = temp;
	temp = *b;
	*b = (*b)->next;
	temp->next = NULL;
	last = *b;
	while (last->next)
		last = last->next;
	last->next = temp;
	write(1, "rr\n", 3);
}
