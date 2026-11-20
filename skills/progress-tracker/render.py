"""Fill the tracker page template and write it as the JSON document the dashboard stores.

Usage: python3 render.py --project "My App" --unit Sprint --units Sprints --out /tmp/index.json
"""
import argparse
import html
import json
import pathlib

parser = argparse.ArgumentParser()
parser.add_argument("--project", required=True, help='Project name, e.g. "Secretary"')
parser.add_argument("--unit", default="Milestone", help="Singular word for a step: Milestone, Sprint, Phase")
parser.add_argument("--units", default=None, help="Plural of --unit (default: --unit + s)")
parser.add_argument("--out", required=True, help="Where to write the JSON document")
args = parser.parse_args()

units = args.units or args.unit + "s"
page = (pathlib.Path(__file__).parent / "template" / "index.html").read_text(encoding="utf-8")
for placeholder, value in {
    "{{PROJECT}}": args.project,
    "{{UNIT}}": args.unit,
    "{{UNITS}}": units,
    "{{units}}": units.lower(),
}.items():
    page = page.replace(placeholder, html.escape(value, quote=True))
assert "{{" not in page, "unfilled placeholder in template"
pathlib.Path(args.out).write_text(json.dumps({"text": page}), encoding="utf-8")
print(args.out)
