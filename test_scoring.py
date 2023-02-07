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


def test_output():
    ranking = {
        "FC Awesome": 1,
        "Grouches": 0,
        "Lions": 5,
        "Snakes": 1,
        "Tarantulas": 6,
    }
    expected_output = []
    with open("expected-output.txt", "r") as output_file:
        # We strip the expected-output.txt string because it contains an extra
        # newline char that will fail the test, but isn' an issue on the command line
        expected_output = output_file.read().strip()
    actual_output = main.format_output(ranking)
    assert actual_output == expected_output
