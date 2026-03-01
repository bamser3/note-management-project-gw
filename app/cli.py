
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

def main():
    parser = argparse.ArgumentParser(description="Notes Manager CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Create note
    create_parser = subparsers.add_parser("add-note")
    create_parser.add_argument("id")
    create_parser.add_argument("title")
    create_parser.add_argument("content")

    # View notes
    subparsers.add_parser("list-notes")

    # Update note
    update_parser = subparsers.add_parser("update-note")
    update_parser.add_argument("id")
    update_parser.add_argument("content")

    # Delete note
    delete_parser = subparsers.add_parser("delete-note")
    delete_parser.add_argument("id")

    args = parser.parse_args()

    if args.command == "add-note":
        note = note_manager.add_note(args.id, args.title, args.content)
        print("Note added:", note.to_dict())

    elif args.command == "list-notes":
        print("Notes:", note_manager.get_notes())

    elif args.command == "update-note":
        success = note_manager.update_note(args.id, args.content)
        print("Updated!" if success else "Note not found.")

    elif args.command == "delete-note":
        success = note_manager.delete_note(args.id)
        print("Deleted!" if success else "Note not found.")


if __name__ == "__main__":

    main()
