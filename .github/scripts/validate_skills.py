#!/usr/bin/env python3
"""Validate every skills/<name>/SKILL.md file.

Checks:
  - Has YAML frontmatter delimited by ---
  - Frontmatter contains required keys: name, description
  - Frontmatter `name` matches the directory name
  - Body is non-empty
No third-party dependencies (parses frontmatter manually).
"""
import os
import re
import sys
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SKILLS_DIR = os.path.join(ROOT, "skills")
REQUIRED = ["name", "description"]


def parse_frontmatter(text):
    if not text.startswith("---"):
        return None
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.DOTALL)
    if not m:
        return None
    fm, body = m.group(1), m.group(2)
    data = {}
    for line in fm.splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if ":" in line:
            k, _, v = line.partition(":")
            data[k.strip()] = v.strip()
    return data, body


def main():
    errors = []
    files = sorted(glob.glob(os.path.join(SKILLS_DIR, "*", "SKILL.md")))
    if not files:
        errors.append("No skills/*/SKILL.md found under %s" % SKILLS_DIR)
    for path in files:
        rel = os.path.relpath(path, ROOT)
        dir_name = os.path.basename(os.path.dirname(path))
        try:
            with open(path, encoding="utf-8") as f:
                text = f.read()
        except Exception as e:  # noqa: BLE001
            errors.append("%s: cannot read (%s)" % (rel, e))
            continue
        parsed = parse_frontmatter(text)
        if parsed is None:
            errors.append("%s: missing or malformed YAML frontmatter" % rel)
            continue
        data, body = parsed
        for key in REQUIRED:
            if key not in data or not data[key]:
                errors.append("%s: missing required frontmatter field '%s'" % (rel, key))
        if "name" in data and data["name"] != dir_name:
            errors.append("%s: frontmatter name '%s' != directory '%s'" % (rel, data["name"], dir_name))
        if not body.strip():
            errors.append("%s: empty body" % rel)

    if errors:
        print("SKILL.md validation FAILED:")
        for e in errors:
            print("  - %s" % e)
        sys.exit(1)
    print("All %d SKILL.md files valid." % len(files))


if __name__ == "__main__":
    main()
