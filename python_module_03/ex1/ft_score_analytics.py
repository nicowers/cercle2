import sys

if __name__ == "__main__":
    try:
        for i in range(1, len(sys.argv) - 1):
            int(sys.argv[i])
        if len(sys.argv) < 2:
            print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        elif len(sys.argv) >= 2:
            list = []
            for i in range(1, len(sys.argv)):
                list.append(int(sys.argv[i]))
            lenght = len(list)
            total_score = sum(list)
            avg = total_score / lenght
            maxi = max(list)
            mini = min(list)
            score_range = maxi - mini
            print("Scores processed:", list)
            print("Total players:",lenght)
            print("Total score:", total_score)
            print("Average score:", avg)
            print("High score:", maxi)
            print("Low score:", mini)
            print("Score range:", score_range)
    except ValueError as e:
        print(f"oops, you typed ’{sys.argv[i]}’ instead of a number")