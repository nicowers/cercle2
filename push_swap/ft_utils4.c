/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_utils4.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ndebavel <ndebavel@student.42lehavre.fr>   +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/16 10:04:15 by ndebavel          #+#    #+#             */
/*   Updated: 2025/12/16 15:42:59 by ndebavel         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	ft_error(t_stack **a)
{
	write(2, "Error\n", 6);
	free_stack(a);
	return (1);
}

void	rotate_both(t_stack **a, t_stack **b, t_stack *n)
{
	while (n->cost_a > 0 && n->cost_b > 0)
	{
		rr(a, b);
		n->cost_a--;
		n->cost_b--;
	}
	while (n->cost_a < 0 && n->cost_b < 0)
	{
		rrr(a, b);
		n->cost_a++;
		n->cost_b++;
	}
}

void	rotate_a(t_stack **a, t_stack *n)
{
	while (n->cost_a != 0)
	{
		if (n->cost_a > 0)
		{
			ra(a);
			n->cost_a--;
		}
		else
		{
			rra(a);
			n->cost_a++;
		}
	}
}

void	rotate_b(t_stack **b, t_stack *n)
{
	while (n->cost_b != 0)
	{
		if (n->cost_b > 0)
		{
			rb(b);
			n->cost_b--;
		}
		else
		{
			rrb(b);
			n->cost_b++;
		}
	}
}

void	execute_move(t_stack **a, t_stack **b, t_stack *node)
{
	if (!a || !b || !node)
		return ;
	rotate_both(a, b, node);
	rotate_a(a, node);
	rotate_b(b, node);
	pa(a, b);
}
