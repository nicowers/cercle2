/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_stack.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ndebavel <ndebavel@student.42lehavre.fr>   +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/21 11:44:37 by ndebavel          #+#    #+#             */
/*   Updated: 2025/12/17 13:52:06 by ndebavel         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_stack_clear(t_stack **lst)
{
	t_stack	*temp;

	while (*lst != NULL)
	{
		temp = (*lst)->next;
		ft_stack_delone(*lst);
		*lst = temp;
	}
	*lst = NULL;
}

void	ft_stack_delone(t_stack *stack)
{
	if (!stack)
		return ;
	free(stack);
}

t_stack	*ft_stack_last(t_stack *lst)
{
	if (lst == NULL)
		return (NULL);
	while (lst->next != NULL)
	{
		lst = lst->next;
	}
	return (lst);
}

t_stack	*ft_stack_new(int value)
{
	t_stack	*newstack;

	newstack = malloc(sizeof(t_stack));
	if (!newstack)
		return (NULL);
	newstack->next = NULL;
	newstack->index = -1;
	newstack->value = value;
	return (newstack);
}

int	ft_stack_size(t_stack *stack)
{
	int	i;

	i = 1;
	if (stack == NULL)
		return (0);
	while (stack->next != NULL)
	{
		i++;
		stack = stack->next;
	}
	return (i);
}
