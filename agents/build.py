"""Build the agent instruction files from one source.

agents/siim-api.md is the only file to edit. This script writes:

  agents/SKILL.md   read by Claude Code when placed at .claude/skills/siim-hackathon-api/SKILL.md
  agents/AGENTS.md  read by OpenAI Codex, GitHub Copilot and other agents from the project root

Usage:
  python agents/build.py          regenerate both files
  python agents/build.py --check  exit 1 if either file is out of date (for review or CI)
"""

from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "siim-api.md"

GENERATED_NOTE = (
    "<!-- Generated from agents/siim-api.md by agents/build.py. Edit the source, not this file. -->\n"
)

SKILL_FRONTMATTER = """---
name: siim-hackathon-api
description: How to call the SIIM Hackathon FHIR and DICOMweb server (hackathon.siim.org) - endpoints, the apikey header, rate and upload limits, status codes, the daily reset, and a Python client that retries correctly. Use whenever code reads or writes FHIR resources or DICOM studies on hackathon.siim.org.
---

"""

AGENTS_HEADER = """# Project notes for AI coding agents

This project uses the SIIM Hackathon server. Follow the reference below whenever
you write code that calls `hackathon.siim.org`.

"""


def demote_headings(markdown: str) -> str:
    """Push every heading down one level, leaving fenced code blocks untouched."""
    lines, in_fence = [], False
    for line in markdown.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
        elif not in_fence and line.startswith("#"):
            line = "#" + line
        lines.append(line)
    return "\n".join(lines) + "\n"


def render(source_text: str) -> dict[Path, str]:
    """Return the full text of each generated file, keyed by its path."""
    body = source_text.rstrip() + "\n"
    agents_body = demote_headings(body)  # sits under the AGENTS.md title
    return {
        HERE / "SKILL.md": SKILL_FRONTMATTER + GENERATED_NOTE + "\n" + body,
        HERE / "AGENTS.md": AGENTS_HEADER + GENERATED_NOTE + "\n" + agents_body,
    }


def main(argv: list[str]) -> int:
    check = "--check" in argv
    outputs = render(SOURCE.read_text(encoding="utf-8"))
    stale = []
    for path, text in outputs.items():
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current == text:
            continue
        if check:
            stale.append(path.name)
        else:
            path.write_text(text, encoding="utf-8", newline="\n")
            print(f"wrote {path.relative_to(HERE.parent)}")
    if stale:
        print("out of date: " + ", ".join(stale) + " (run python agents/build.py)")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
