
import argparse
from notes.note_manager import NoteManager

note_manager = NoteManager()

def main():
    parser = argparse.ArgumentParser(description="Notes Manager CLI")
    subparsers = parser.add_subparsers(dest="command")

    
    subparsers.add_parser("list-notes")

    args = parser.parse_args()

    if args.command == "list-notes":
        print("Notes:", note_manager.get_notes())

if __name__ == "__main__":
    main()
