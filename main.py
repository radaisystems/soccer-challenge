import re


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
