import subprocess
from pathlib import Path

import pytask


@pytask.mark.depends_on([
    "docs.md",
])
@pytask.mark.produces("docs.pdf")
def task_pandoc_docs():
    result = subprocess.run([
        "pandoc",
        "-o", "docs.pdf",
        "-f", "markdown+tex_math_single_backslash",
        "-V", "documentclass:scrartcl",
        "docs.md"
    ], capture_output=True, cwd=Path(__file__).parent)

    print()
    print(result.stdout)
    result.check_returncode()
