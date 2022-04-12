from pathlib import Path

import pytest

from pyroll import solve
from pyroll.ui.report import Report

THIS_DIR = Path(__file__).parent


def test_solve(tmp_path: Path):
    import pyroll.ui.cli.res.input_trio as input_py
    import pyroll_hitchcook_roll_flattening

    sequence = input_py.sequence

    solve(sequence, input_py.in_profile)

    report = Report()

    rendered = report.render(sequence)
    print()

    report_file = tmp_path / "report.html"
    report_file.write_text(rendered)
    print(report_file)


def test_solve_repeated(tmp_path: Path):
    for i in range(20):
        test_solve(tmp_path)
