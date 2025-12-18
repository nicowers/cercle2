/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ndebavel <ndebavel@student.42lehavre.fr>   +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/05 13:56:15 by ndebavel          #+#    #+#             */
/*   Updated: 2025/12/17 13:36:09 by ndebavel         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	sort_3(t_stack **a)
{
	int	first;
	int	second;
	int	third;

	first = (*a)->value;
	second = (*a)->next->value;
	third = (*a)->next->next->value;
	if (first > second && second < third && first < third)
		sa(a);
	else if (first > second && second < third && first > third)
		ra(a);
	else if (first < second && second > third && first > third)
		rra(a);
	else if (first < second && second > third && first < third)
	{
		sa(a);
		ra(a);
	}
	else if (first > second && second > third)
	{
		sa(a);
		rra(a);
	}
}

// int	find_min_pos(t_stack *a)
// {
// 	int	min;
// 	int	pos;
// 	int	i;
//
// 	min = a->value;
// 	pos = 0;
// 	i = 0;
// 	while (a)
// 	{
// 		if (a->value < min)
// 		{
// 			min = a->value;
// 			pos = i;
// 		}
// 		a = a->next;
// 		i++;
// 	}
// 	return (pos);
// }

// void	bring_min_to_top(t_stack **a, int pos)
// {
// 	int	size;
//
// 	size = ft_stack_size(*a);
// 	if (pos <= size / 2)
// 	{
// 		while (pos--)
// 			ra(a);
// 	}
// 	else
// 	{
// 		pos = size - pos;
// 		while (pos--)
// 			rra(a);
// 	}
// }

void	sort_2(t_stack **a)
{
	if (!a || !*a || !(*a)->next)
		return ;
	if ((*a)->value > (*a)->next->value)
		sa(a);
}
