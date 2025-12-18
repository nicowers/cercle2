/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ndebavel <ndebavel@student.42lehavre.fr>   +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/04 16:14:11 by ndebavel          #+#    #+#             */
/*   Updated: 2025/12/17 14:02:47 by ndebavel         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	algo(t_stack **a, t_stack **b)
{
	int	size;

	size = ft_stack_size(*a);
	if (size == 1)
		return ;
	if (size == 2)
		sort_2(a);
	else if (size == 3)
		sort_3(a);
	else
		turk_sort(a, b);
}

int	main(int argc, char **argv)
{
	t_stack	*a;
	t_stack	*b;
	char	**args;
	int		to_free;

	a = NULL;
	b = NULL;
	if (argc < 2)
		return (0);
	args = init_args(argc, argv, &to_free);
	if (!args || !parse_input(args, &a) || check_dup(a))
	{
		if (to_free)
			ft_free_split(args);
		return (ft_error(&a));
	}
	if (!is_sorted(a))
		algo(&a, &b);
	free_stack(&a);
	free_stack(&b);
	if (to_free)
		ft_free_split(args);
	return (0);
}

int	parse_input(char **argv, t_stack **a)
{
	int		i;
	long	val;
	t_stack	*new;

	i = 0;
	*a = NULL;
	while (argv[i])
	{
		if (!is_valid_number(argv[i]))
			return (0);
		val = ft_atol(argv[i]);
		if (val > 2147483647 || val < -2147483648)
			return (0);
		new = malloc(sizeof(t_stack));
		if (!new)
			return (0);
		new->value = (int)val;
		new->index = -1;
		new->pos = 0;
		new->next = NULL;
		ft_stack_add_back(a, new);
		i++;
	}
	return (1);
}

char	**init_args(int argc, char **argv, int *to_free)
{
	char	**args;
	char	**tmp;
	int		i;
	int		j;
	int		k;

	args = NULL;
	i = 1;
	k = 0;
	*to_free = 1;
	while (i < argc)
	{
		tmp = ft_split(argv[i], ' ');
		if (!tmp)
			return (NULL);
		j = 0;
		while (tmp[j])
			args = ft_tab_add(args, tmp[j++], &k);
		ft_free_split(tmp);
		i++;
	}
	return (args);
}

char	**ft_tab_add(char **tab, char *str, int *size)
{
	char	**new;
	int		i;

	new = malloc(sizeof(char *) * (*size + 2));
	if (!new)
		return (NULL);
	i = 0;
	while (i < *size)
	{
		new[i] = tab[i];
		i++;
	}
	new[i] = ft_strdup(str);
	new[i + 1] = NULL;
	free(tab);
	(*size)++;
	return (new);
}
