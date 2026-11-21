"""Render the tracker template as the JSON document stored by the dashboard.

Example:
    python3 render.py --project "My App" --unit Sprint --units Sprints --out /tmp/index.json
"""

import argparse
import html
import json
import pathlib
import re

PLACEHOLDER = re.compile(r"{{[A-Za-z_]+}}")


def non_empty(value):
    value = value.strip()
    if not value:
        raise argparse.ArgumentTypeError("must not be empty")
    return value


def render_page(project, unit, units):
    template_path = pathlib.Path(__file__).parent / "template" / "index.html"
    template = template_path.read_text(encoding="utf-8")
    values = {
        "{{PROJECT}}": project,
        "{{UNIT}}": unit,
        "{{UNITS}}": units,
        "{{units}}": units.lower(),
    }
    unknown = set(PLACEHOLDER.findall(template)) - values.keys()
    if unknown:
        raise ValueError("template contains unknown placeholders: " + ", ".join(sorted(unknown)))

    return PLACEHOLDER.sub(
        lambda match: html.escape(values[match.group(0)], quote=True), template
    )


def main():
    parser = argparse.ArgumentParser(
        description="Render the build tracker page as an artifact document."
    )
    parser.add_argument("--project", required=True, type=non_empty, help='Project name, e.g. "Secretary"')
    parser.add_argument(
        "--unit",
        default="Milestone",
        type=non_empty,
        help="Singular word for a step: Milestone, Sprint, Phase",
    )
    parser.add_argument(
        "--units", default=None, type=non_empty, help="Plural of --unit (default: --unit + s)"
    )
    parser.add_argument("--out", required=True, type=non_empty, help="Where to write the JSON document")
    args = parser.parse_args()

    units = args.units or args.unit + "s"
    try:
        page = render_page(args.project, args.unit, units)
    except ValueError as error:
        parser.error(str(error))

    output = pathlib.Path(args.out).expanduser()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps({"text": page}), encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
