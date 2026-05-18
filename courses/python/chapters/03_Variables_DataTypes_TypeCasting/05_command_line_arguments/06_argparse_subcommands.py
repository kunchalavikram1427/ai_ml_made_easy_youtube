"""
argparse Subcommands — Building Git-Style CLIs
================================================
Run: python3 06_argparse_subcommands.py add file1.py file2.py
     python3 06_argparse_subcommands.py commit -m "Initial commit"
     python3 06_argparse_subcommands.py log --count 5
     python3 06_argparse_subcommands.py status --short
     python3 06_argparse_subcommands.py --help
     python3 06_argparse_subcommands.py add --help

Demonstrates building CLI tools with multiple subcommands,
similar to how git, docker, and kubectl work.

Demonstrates:
- add_subparsers() for subcommands
- Each subcommand with its own arguments
- Global arguments that work across all subcommands
- Routing to handler functions with if/elif
"""

import argparse
import sys


# =============================================================================
# SUBCOMMAND HANDLERS
# =============================================================================

def handle_add(args):
    """Handle the 'add' subcommand."""
    print(f"\n  [ADD] Staging files:")
    for f in args.files:
        print(f"    + {f}")
    if args.force:
        print(f"    (force mode: ignoring .gitignore)")
    if args.verbose:
        print(f"    [VERBOSE] {len(args.files)} file(s) staged")


def handle_commit(args):
    """Handle the 'commit' subcommand."""
    print(f"\n  [COMMIT] Creating commit:")
    print(f"    Message: \"{args.message}\"")
    if args.amend:
        print(f"    (amending previous commit)")
    if args.author:
        print(f"    Author: {args.author}")
    if args.verbose:
        print(f"    [VERBOSE] Commit created successfully")


def handle_log(args):
    """Handle the 'log' subcommand."""
    print(f"\n  [LOG] Showing commit history:")
    # Simulated log entries
    fake_commits = [
        ("a1b2c3d", "Fix login bug", "Vikram"),
        ("e4f5g6h", "Add user dashboard", "Vikram"),
        ("i7j8k9l", "Update dependencies", "Alice"),
        ("m0n1o2p", "Initial commit", "Vikram"),
        ("q3r4s5t", "Add README", "Bob"),
    ]

    count = args.count if args.count else len(fake_commits)
    for _, (hash_, msg, author) in enumerate(fake_commits[:count]):
        if args.oneline:
            print(f"    {hash_} {msg}")
        else:
            print(f"    commit {hash_}")
            print(f"    Author: {author}")
            print(f"    Message: {msg}")
            print()

    if args.verbose:
        print(f"    [VERBOSE] Showing {min(count, len(fake_commits))} of {len(fake_commits)} commits")


def handle_status(args):
    """Handle the 'status' subcommand."""
    # Simulated status
    staged = ["README.md", "src/main.py"]
    modified = ["src/utils.py"]
    untracked = ["notes.txt", "temp/debug.log"]

    if args.short:
        print(f"\n  [STATUS] (short format)")
        for f in staged:
            print(f"    A  {f}")
        for f in modified:
            print(f"    M  {f}")
        for f in untracked:
            print(f"    ?? {f}")
    else:
        print(f"\n  [STATUS]")
        print(f"    Changes staged for commit:")
        for f in staged:
            print(f"      new file: {f}")
        print(f"\n    Changes not staged:")
        for f in modified:
            print(f"      modified: {f}")
        print(f"\n    Untracked files:")
        for f in untracked:
            print(f"      {f}")

    if args.verbose:
        print(f"\n    [VERBOSE] {len(staged)} staged, {len(modified)} modified, {len(untracked)} untracked")


# =============================================================================
# PARSER SETUP & MAIN
# =============================================================================

def main():
    # Main parser
    parser = argparse.ArgumentParser(
        description="Mini-Git: A simplified git-like CLI tool (demo)",
        epilog="Run '%(prog)s <command> --help' for help on a specific command"
    )

    # Global arguments (work with all subcommands)
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output"
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.0"
    )

    # Create subcommand parsers
    subparsers = parser.add_subparsers(
        dest="command",
        title="commands",
        description="Available commands"
    )

    # --- 'add' subcommand ---
    add_parser = subparsers.add_parser(
        "add",
        help="Stage files for commit"
    )
    add_parser.add_argument(
        "files",
        nargs="+",
        help="Files to stage"
    )
    add_parser.add_argument(
        "-f", "--force",
        action="store_true",
        help="Force add (ignore .gitignore)"
    )

    # --- 'commit' subcommand ---
    commit_parser = subparsers.add_parser(
        "commit",
        help="Create a new commit"
    )
    commit_parser.add_argument(
        "-m", "--message",
        required=True,
        help="Commit message"
    )
    commit_parser.add_argument(
        "--amend",
        action="store_true",
        help="Amend the previous commit"
    )
    commit_parser.add_argument(
        "--author",
        help="Override commit author"
    )

    # --- 'log' subcommand ---
    log_parser = subparsers.add_parser(
        "log",
        help="Show commit history"
    )
    log_parser.add_argument(
        "-n", "--count",
        type=int,
        default=None,
        help="Number of commits to show"
    )
    log_parser.add_argument(
        "--oneline",
        action="store_true",
        help="Show each commit on one line"
    )

    # --- 'status' subcommand ---
    status_parser = subparsers.add_parser(
        "status",
        help="Show working tree status"
    )
    status_parser.add_argument(
        "-s", "--short",
        action="store_true",
        help="Show short format"
    )

    # Parse and execute
    args = parser.parse_args()

    # If no subcommand given, show help
    if not args.command:
        parser.print_help()
        sys.exit(1)

    print("=" * 50)
    print(f"  MINI-GIT: '{args.command}' command")
    print("=" * 50)

    # Call the appropriate handler based on the subcommand
    if args.command == "add":
        handle_add(args)
    elif args.command == "commit":
        handle_commit(args)
    elif args.command == "log":
        handle_log(args)
    elif args.command == "status":
        handle_status(args)

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
