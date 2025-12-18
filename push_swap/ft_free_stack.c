/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_free_stack.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ndebavel <ndebavel@student.42lehavre.fr>   +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/28 16:18:53 by ndebavel          #+#    #+#             */
/*   Updated: 2025/12/04 16:41:21 by ndebavel         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	free_stack(t_stack **value)
{
	t_stack	*temp;
	t_stack	*current;

	current = *value;
	while (current)
	{
		temp = current->next;
		free(current);
		current = temp;
	}
	current = NULL;
}
