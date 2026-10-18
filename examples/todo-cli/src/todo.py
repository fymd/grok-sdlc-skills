"""Minimal CLI todo app — reference example for grok-sdlc-skills.

Built through the full SDLC flow (spec -> plan -> build -> verify -> review -> ship).
Stdlib-only, no third-party dependencies.
"""
import argparse
import json
import sys
from pathlib import Path

DEFAULT_STORE = Path.home() / ".todo-cli.json"


def load(store: Path) -> list:
    if not store.exists():
        return []
    try:
        return json.loads(store.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []


def save(store: Path, items: list) -> None:
    store.write_text(json.dumps(items, indent=2, ensure_ascii=False), encoding="utf-8")


def add(store: Path, title: str) -> dict:
    items = load(store)
    item = {"id": (items[-1]["id"] + 1) if items else 1, "title": title, "done": False}
    items.append(item)
    save(store, items)
    return item


def list_items(store: Path) -> list:
    return load(store)


def complete(store: Path, item_id: int) -> bool:
    items = load(store)
    for it in items:
        if it["id"] == item_id:
            it["done"] = True
            save(store, items)
            return True
    return False


def remove(store: Path, item_id: int) -> bool:
    items = load(store)
    kept = [it for it in items if it["id"] != item_id]
    if len(kept) == len(items):
        return False
    save(store, kept)
    return True


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="todo", description="Minimal CLI todo list")
    p.add_argument("--store", type=Path, default=DEFAULT_STORE, help="path to JSON store")
    sub = p.add_subparsers(dest="cmd", required=True)

    pa = sub.add_parser("add", help="add a task")
    pa.add_argument("title")

    sub.add_parser("list", help="list tasks")

    pc = sub.add_parser("done", help="mark a task done")
    pc.add_argument("id", type=int)

    pr = sub.add_parser("rm", help="remove a task")
    pr.add_argument("id", type=int)

    args = p.parse_args(argv)
    if args.cmd == "add":
        item = add(args.store, args.title)
        print(f"added #{item['id']}: {item['title']}")
    elif args.cmd == "list":
        for it in list_items(args.store):
            mark = "x" if it["done"] else " "
            print(f"[{mark}] {it['id']}: {it['title']}")
    elif args.cmd == "done":
        print("ok" if complete(args.store, args.id) else f"no such id {args.id}")
    elif args.cmd == "rm":
        print("removed" if remove(args.store, args.id) else f"no such id {args.id}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
