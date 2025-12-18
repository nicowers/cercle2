/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ndebavel <ndebavel@student.42lehavre.fr>   +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/24 10:34:30 by ndebavel          #+#    #+#             */
/*   Updated: 2025/12/17 14:03:09 by ndebavel         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <stdlib.h>
# include <stdio.h>
# include <unistd.h>
# include <limits.h>

typedef struct s_stack
{
	int				value;
	int				index;
	int				pos;
	int				target_pos;
	int				cost_a;
	int				cost_b;
	struct s_stack	*next;
}		t_stack;

void	pa(t_stack **a, t_stack **b);
void	pb(t_stack **a, t_stack **b);
void	rra(t_stack **a);
void	rrb(t_stack **b);
void	rrr(t_stack **a, t_stack **b);
void	ra(t_stack **a);
void	rb(t_stack **b);
void	rr(t_stack **a, t_stack **b);
void	sa(t_stack **a);
void	sb(t_stack **b);
void	ss(t_stack **a, t_stack**b);
void	free_stack(t_stack **value);
void	ft_stack_add_back(t_stack **stack, t_stack *new);
void	ft_stack_add_front(t_stack **stack, t_stack *new);
void	ft_stack_clear(t_stack **lst);
void	ft_stack_delone(t_stack *lst);
t_stack	*ft_stack_last(t_stack *lst);
t_stack	*ft_stack_new(int value);
int		ft_stack_size(t_stack *stack);
long	ft_atol(const char *str);
int		count_word(char const *s, char c);
char	*ft_strdup_split(const char *src, char c);
void	ft_freeall(char **tab, int j);
char	**ft_split(char const *s, char c);
int		is_valid_number(char *str);
int		check_dup(t_stack *a);
int		ft_error(t_stack **a);
void	ft_free_split(char **tab);
int		is_sorted(t_stack *a);
void	sort_2(t_stack **a);
void	sort_3(t_stack **a);
void	turk_sort(t_stack **a, t_stack **b);
int		parse_input(char **argv, t_stack **a);
void	set_positions(t_stack *stack);
int		get_lowest_index_pos(t_stack *stack);
void	set_target_positions(t_stack *a, t_stack *b);
void	set_costs(t_stack *a, t_stack *b);
t_stack	*get_cheapest(t_stack *b);
void	execute_move(t_stack **a, t_stack **b, t_stack *node);
void	do_cheapest_move(t_stack **a, t_stack **b);
void	final_rotate(t_stack **a);
void	index_stack(t_stack *stack);
void	push_to_b(t_stack **a, t_stack **b);
void	rotate_both(t_stack **a, t_stack **b, t_stack *n);
void	rotate_a(t_stack **a, t_stack *n);
void	rotate_b(t_stack **b, t_stack *n);
char	**init_args(int argc, char **argv, int *to_free);
char	**ft_tab_add(char **tab, char *str, int *size);
char	*ft_strdup(const char *str);

#endif