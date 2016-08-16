"""
Determines the user's ranking in correspondence to their score
"""
__author__ = 'Gareth'


def main():
    score_to_ranking(float(input("Enter score: ")))


def score_to_ranking(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score > 90:
        print("Excellent")
    elif score > 50:
        print("Passable")
    else:
        print("Bad")


if __name__ == "__main__":
    main()