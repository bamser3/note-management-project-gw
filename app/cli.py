import argparse
from notes.note_manager import NoteManager
from auth.auth_manager_class import User
from storage.storage_class import Storage
from auth.auth_manager_class import User
from notes.note_class import Note

storage = Storage()

note_manager = NoteManager(storage)


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
        notes = storage.load_notes()
        note = Note(args.id, args.title, args.content)
        notes.append(note)
        storage.save_notes(notes)
        print("Note saved:", note.to_dict())

    elif args.command == "list-notes":
        print("Notes:", note_manager.get_notes())

    elif args.command == "update-note":
        notes = storage.load_notes()
        for note in notes:
            if note.id == args.id:
                note.update_content(args.content)
                storage.save_notes(notes)
                print("Updated!")
                break
        else:
            print("Note not found.")

    elif args.command == "delete-note":
        notes = storage.load_notes()
        new_notes = [note for note in notes if note.id != args.id]

        if len(new_notes) != len(notes):
            storage.save_notes(new_notes)
            print("Deleted!")
        else:
            print("Note not found.")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()