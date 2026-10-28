import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    scores = []
    for score in sys.argv[1:]:
        try:
            scores.append(int(score))
        except ValueError:
            print(f"Invalid parameter: '{score}'")
    if len(scores) > 0:
        total_players = len(scores)
        total_score = sum(scores)
        average_score = total_score / len(scores)
        highest_score = max(scores)
        lowest_score = min(scores)
        score_range = highest_score - lowest_score
        print(f"Scores processed: {scores}")
        print(f"Total players: {total_players}")
        print(f"Total score: {total_score}")
        print(f"Average score: {average_score:.1f}")
        print(f"High score: {highest_score}")
        print(f"Low score: {lowest_score}")
        print(f"Score range: {score_range}")
    else:
        print("No scores provided. Usage: python ", end="")
        print("ft_score_analytics.py <score1> <score2> ...")
