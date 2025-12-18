CC = cc
NAME = push_swap
CFLAGS = -Wall -Wextra -Werror
SRC = main.c push.c reverse_rotate.c rotate.c swap.c \
ft_free_stack.c ft_stack_add.c ft_stack.c\
ft_atol.c ft_split.c ft_utils1.c ft_utils2.c ft_utils3.c \
sort.c ft_utils4.c
OBJ = $(SRC:.c=.o)

all: $(NAME)
$(NAME): $(OBJ)
	$(CC) $(OBJ) -o $(NAME)

clean:
	rm -f $(OBJ)

fclean: clean
	rm -f $(NAME)

re: fclean all
