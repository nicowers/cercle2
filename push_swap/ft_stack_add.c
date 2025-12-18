/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_stack_add_back.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ndebavel <ndebavel@student.42lehavre.fr>   +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/21 10:58:04 by ndebavel          #+#    #+#             */
/*   Updated: 2025/12/17 13:51:43 by ndebavel         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_stack_add_back(t_stack **stack, t_stack *new)
{
	t_stack	*last;

	if (!stack || !new)
		return ;
	last = ft_stack_last(*stack);
	if (last == NULL)
	{
		ft_stack_add_front(stack, new);
	}
	else
		last->next = new;
}

void	ft_stack_add_front(t_stack **stack, t_stack *new)
{
	if (!new)
		return ;
	if (stack != NULL)
	{
		new->next = *stack;
		*stack = new;
		return ;
	}
}
