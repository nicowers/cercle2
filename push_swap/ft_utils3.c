/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_utils3.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ndebavel <ndebavel@student.42lehavre.fr>   +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/15 13:35:19 by ndebavel          #+#    #+#             */
/*   Updated: 2025/12/18 09:36:02 by ndebavel         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	turk_sort(t_stack **a, t_stack **b)
{
	int	size;

	size = ft_stack_size(*a);
	if (!a || !*a)
		return ;
	index_stack(*a);
	push_to_b(a, b);
	sort_3(a);
	while (*b)
	{
		set_positions(*a);
		set_positions(*b);
		set_target_positions(*a, *b);
		set_costs(*a, *b);
		do_cheapest_move(a, b);
	}
	final_rotate(a);
}

t_stack	*get_cheapest(t_stack *b)
{
	t_stack	*tmp;
	t_stack	*cheapest;
	int		min;
	int		cost;

	tmp = b;
	cheapest = b;
	min = abs(b->cost_a) + abs(b->cost_b);
	while (tmp)
	{
		cost = abs(tmp->cost_a) + abs(tmp->cost_b);
		if (cost < min)
		{
			min = cost;
			cheapest = tmp;
		}
		tmp = tmp->next;
	}
	return (cheapest);
}

void	do_cheapest_move(t_stack **a, t_stack **b)
{
	t_stack	*cheapest;

	if (!b || !*b)
		return ;
	cheapest = get_cheapest(*b);
	execute_move(a, b, cheapest);
}

void	final_rotate(t_stack **a)
{
	int	size;

	if (!a || !*a)
		return ;
	size = ft_stack_size(*a);
	while ((*a)->index != 0)
	{
		if (get_lowest_index_pos(*a) > size / 2)
			rra(a);
		else
			ra(a);
	}
}

void	index_stack(t_stack *stack)
{
	t_stack	*tmp;
	t_stack	*min_node;
	int		index;

	index = 0;
	while (1)
	{
		tmp = stack;
		min_node = NULL;
		while (tmp)
		{
			if (tmp->index == -1 && (!min_node || tmp->value < min_node->value))
				min_node = tmp;
			tmp = tmp->next;
		}
		if (!min_node)
			break ;
		min_node->index = index++;
	}
}
