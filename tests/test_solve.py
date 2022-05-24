import logging
from pathlib import Path

from pyroll.core import solve
from pyroll.ui import Reporter


def test_solve(tmp_path: Path, caplog):
    caplog.set_level(logging.DEBUG, "pyroll")

    from pyroll import hitchcock_roll_flattening

    from pyroll.ui.cli.res import input_trio

    solve(input_trio.sequence, input_trio.in_profile)

    report = Reporter().render(input_trio.sequence)

    report_file = tmp_path / "report.html"
    report_file.write_text(report)
    print()
    print(report_file)

    print()
    print(caplog.text)
