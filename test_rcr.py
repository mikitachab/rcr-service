import pytest

from rcr import command_log_to_rcr_map


@pytest.mark.parametrize(
    "command_log, rcr_map",
    [
        (
            ["LEFT", "GRAB", "LEFT", "BACK", "LEFT", "BACK", "LEFT"],
            {"GRAB": "00", "BACK": "01", "LEFT": "1"},
        ),
        (
            [
                "DOWN",
                "RIGHT",
                "UP",
                "RIGHT",
                "RIGHT",
                "LEFT",
                "GRAB",
                "LEFT",
                "LEFT",
                "LEFT",
                "UP",
                "DOWN",
                "RIGHT",
                "LEFT",
                "UP",
                "DROP",
            ],
            {
                "GRAB": "1010",
                "DROP": "1011",
                "DOWN": "100",
                "UP": "00",
                "RIGHT": "01",
                "LEFT": "11",
            },
        ),
    ],
)
def test_commands_to_rcr_codes(command_log, rcr_map):
    assert command_log_to_rcr_map(command_log) == rcr_map
