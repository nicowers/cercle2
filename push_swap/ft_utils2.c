/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_utils2.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ndebavel <ndebavel@student.42lehavre.fr>   +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/15 13:04:15 by ndebavel          #+#    #+#             */
/*   Updated: 2025/12/18 09:36:35 by ndebavel         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	set_positions(t_stack *stack)
{
	int	i;

	i = 0;
	while (stack)
	{
		stack->pos = i;
		i++;
		stack = stack->next;
	}
}

int	get_lowest_index_pos(t_stack *stack)
{
	int	lowest_index;
	int	lowest_pos;

	lowest_index = 2147483647;
	lowest_pos = 0;
	while (stack)
	{
		if (stack->index < lowest_index)
		{
			lowest_index = stack->index;
			lowest_pos = stack->pos;
		}
		stack = stack->next;
	}
	return (lowest_pos);
}

void	set_target_positions(t_stack *a, t_stack *b)
{
	t_stack	*tmp_a;
	int		target_index;

	while (b)
	{
		target_index = 2147483647;
		b->target_pos = 0;
		tmp_a = a;
		while (tmp_a)
		{
			if (tmp_a->index > b->index
				&& tmp_a->index < target_index)
			{
				target_index = tmp_a->index;
				b->target_pos = tmp_a->pos;
			}
			tmp_a = tmp_a->next;
		}
		if (target_index == 2147483647)
			b->target_pos = get_lowest_index_pos(a);
		b = b->next;
	}
}

void	set_costs(t_stack *a, t_stack *b)
{
	int	size_a;
	int	size_b;

	size_a = ft_stack_size(a);
	size_b = ft_stack_size(b);
	while (b)
	{
		b->cost_b = b->pos;
		if (b->pos > size_b / 2)
			b->cost_b = b->pos - size_b;
		b->cost_a = b->target_pos;
		if (b->target_pos > size_a / 2)
			b->cost_a = b->target_pos - size_a;
		b = b->next;
	}
}

void	push_to_b(t_stack **a, t_stack **b)
{
	int	size;
	int	pushed;

	size = ft_stack_size(*a);
	pushed = 0;
	while (size > 6 && pushed < size / 2)
	{
		if ((*a)->index <= size / 2)
		{
			pb(a, b);
			pushed++;
		}
		else
			ra(a);
		size = ft_stack_size(*a);
	}
	while (ft_stack_size(*a) > 3)
		pb(a, b);
}
