/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   swap.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ndebavel <ndebavel@student.42lehavre.fr>   +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/24 10:14:07 by ndebavel          #+#    #+#             */
/*   Updated: 2025/12/08 09:58:08 by ndebavel         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	sa(t_stack **a)
{
	t_stack	*temp1;
	t_stack	*temp2;

	if (!a || !*a || !(*a)->next)
		return ;
	temp1 = *a;
	temp2 = temp1->next;
	temp1->next = temp2->next;
	temp2->next = temp1;
	*a = temp2;
	write(1, "sa\n", 3);
}

void	sb(t_stack **b)
{
	t_stack	*temp1;
	t_stack	*temp2;

	if (!b || !*b || !(*b)->next)
		return ;
	temp1 = *b;
	temp2 = temp1->next;
	temp1->next = temp2->next;
	temp2->next = temp1;
	*b = temp2;
	write(1, "sb\n", 3);
}

void	ss(t_stack **a, t_stack**b)
{
	t_stack	*temp1;
	t_stack	*temp2;

	if (!a || !*a || !(*a)->next)
		return ;
	if (!b || !*b || !(*b)->next)
		return ;
	temp1 = *a;
	temp2 = temp1->next;
	temp1->next = temp2->next;
	temp2->next = temp1;
	*a = temp2;
	temp1 = *b;
	temp2 = temp1->next;
	temp1->next = temp2->next;
	temp2->next = temp1;
	*b = temp2;
	write(1, "ss\n", 3);
}
