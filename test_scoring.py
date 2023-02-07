import main

SAMPLE_INPUT_FILE_NAME = "sample-input.txt"


def test_parse_input():
    expected = {
        "FC Awesome": 1,
        "Grouches": 0,
        "Lions": 5,
        "Snakes": 1,
        "Tarantulas": 6,
    }
    lines = []
    with open(SAMPLE_INPUT_FILE_NAME, "r") as input_file:
        lines = input_file.readlines()
    actual = main.parse_input(lines)
    assert actual == expected

