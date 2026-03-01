import argparse
from notes.note_manager import NoteManager
from auth.auth_manager_class import User
from storage.storage_class import Storage
from auth.auth_manager_class import User

storage = Storage()

note_manager = NoteManager()


def main():
    parser = argparse.ArgumentParser(
        description="Notes Manager CLI",
        epilog="""
Examples:

Add a user:
  python3 cli.py add-user Peter peter@gmail.com password123

Add a note:
  python3 cli.py add-note 1 "Shopping List" "Buy milk and eggs"

List notes:
  python3 cli.py list-notes

Update a note:
  python3 cli.py update-note 1 "Updated content"

Delete a note:
  python3 cli.py delete-note 1
        """,
        formatter_class=argparse.RawTextHelpFormatter
    )

    subparsers = parser.add_subparsers(dest="command")

    user_parser = subparsers.add_parser("add-user")
    user_parser.add_argument("name")
    user_parser.add_argument("email")
    user_parser.add_argument("password")

    create_parser = subparsers.add_parser("add-note")
    create_parser.add_argument("id")
    create_parser.add_argument("title")
    create_parser.add_argument("content")

    subparsers.add_parser("list-notes")

    update_parser = subparsers.add_parser("update-note")
    update_parser.add_argument("id")
    update_parser.add_argument("content")

    delete_parser = subparsers.add_parser("delete-note")
    delete_parser.add_argument("id")

    args = parser.parse_args()

    if args.command == "add-user":
        user = User(args.name, args.email, args.password)
        users = storage.load_users()
        users.append(user)
        storage.save_users(users)
        print("User saved:", user.to_dict())

    elif args.command == "add-note":
        note = note_manager.add_note(args.id, args.title, args.content)
        notes = storage.load_notes()
        notes.append(note)
        storage.save_notes(notes)
        print("Note saved:", note.to_dict())

    elif args.command == "list-notes":
        print("Notes:", note_manager.get_notes())

    elif args.command == "update-note":
        success = note_manager.update_note(args.id, args.content)
        print("Updated!" if success else "Note not found.")

    elif args.command == "delete-note":
        success = note_manager.delete_note(args.id)
        print("Deleted!" if success else "Note not found.")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()