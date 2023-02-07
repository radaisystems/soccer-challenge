import re
import argparse
import sys


def parse_input(lines: list[str]) -> dict:
    """Parse the input file and return a dictionary of team names
    and their league points
    """
    regex = re.compile(
        r"(?P<teamA>[A-Za-z]*)[\s]+(?P<scoreA>[\d]+),[\s]+(?P<teamB>[A-Za-z\s]*)[\s]+(?P<scoreB>[\d]+)"
    )
    scores = {}
    for line in lines:
        team_scores = re.match(regex, line)
        score_a = int(team_scores["scoreA"])
        score_b = int(team_scores["scoreB"])
        if score_a != score_b:
            winning = 1
            if score_b > score_a:
                winning = 3
            # A win is worth 3 points for the winning team, and 0 for the losing team
            scores[team_scores[winning]] = (
                scores.setdefault(team_scores[winning], 0) + 3
            )
            scores[team_scores[4 - winning]] = scores.setdefault(
                team_scores[4 - winning], 0
            )
        elif team_scores["scoreA"] == team_scores["scoreB"]:
            # A tie is worth 1 point for both teams
            scores[team_scores["teamA"]] = (
                scores.setdefault(team_scores["teamA"], 0) + 1
            )
            scores[team_scores["teamB"]] = (
                scores.setdefault(team_scores["teamB"], 0) + 1
            )
    return scores


def format_output(ranking: dict) -> list[str]:
    """Format the ranked teams for output"""
    ranked = sorted(ranking.items(), key=lambda x: (-x[1], x[0]))
    output = []
    place = 1
    for idx, team in enumerate(ranked):
        if idx > 0 and team[1] != ranked[idx - 1][1]:
            place = idx + 1
        output.append(f"{place}. {team[0]}, {team[1]} pt{'s' if team[1] != 1 else ''}")
    return "\n".join(output) + "\n"


def main():
    parser = argparse.ArgumentParser(
        description="Calculate and display a ranking table for a soccer league."
    )
    parser.add_argument(
        "file",
        nargs="?",
        help="Input file, stdin if empty",
        type=argparse.FileType("r"),
        default=sys.stdin,
    )
    args = parser.parse_args()

    if args.file.isatty():
        # Print the help if we didn't get a file arg or anything on stdin
        parser.print_help()
        return 0

    lines = args.file.readlines()
    print(format_output(parse_input(lines)))
    return 0


if __name__ == "__main__":
    main()
