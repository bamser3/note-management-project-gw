from storage.storage_class import Storage
from notes.note_manager import NoteManager
from auth.auth_manager_class import AuthManager
from notes.note_class import Note
import questionary
import uuid

# Initialize storage, managers
storage = Storage()
note_manager = NoteManager(storage)
auth_manager = AuthManager(storage)


def register():
    print("\n Register")
    name = questionary.text("Enter your name:").ask()
    email = questionary.text("Enter your email:").ask()
    password = questionary.password("Enter your password:").ask()
    if auth_manager.register(name, email, password, role="user"):
        print(f"User `{name}` registered successfully.")


def login():
    print("\n Login")
    email = questionary.text("Enter your email:").ask()
    password = questionary.password("Enter your password:").ask()
    if auth_manager.login(email, password):
        print(f"Logged in as {auth_manager.logged_in_user.name}")
        return True
    return False


def add_note():
    print("\n Add Note")
    title = questionary.text("Enter note title:").ask()
    content = questionary.text("Enter note content:").ask()
    note = note_manager.add_note(title, content, auth_manager.logged_in_user)
    print("Note saved:", note.to_dict())


def list_notes():
    print("\n Your Notes ")
    notes = [
        note.to_dict()
        for note in note_manager.notes.values()
        if note.user_id == auth_manager.logged_in_user.id or auth_manager.is_admin()
    ]
    if notes:
        for n in notes:
            print(n)
    else:
        print("No notes found.")


def update_note():
    note_id = questionary.text("Enter the note ID to update:").ask()
    note = note_manager.notes.get(note_id)
    if not note:
        print("Note not found.")
        return
    if note.user_id != auth_manager.logged_in_user.id and not auth_manager.is_admin():
        print("You cannot edit this note.")
        return
    new_content = questionary.text("Enter new content:").ask()
    note.update_content(new_content)
    note_manager._save()
    print("Note updated!")


def delete_note():
    note_id = questionary.text("Enter the note ID to delete:").ask()
    note = note_manager.notes.get(note_id)
    if not note:
        print("Note not found.")
        return
    if note.user_id != auth_manager.logged_in_user.id and not auth_manager.is_admin():
        print("You cannot delete this note.")
        return
    del note_manager.notes[note_id]
    note_manager._save()
    print("Note deleted!")


def main_menu():
    while True:
        choice = questionary.select(
            "Select an option:",
            choices=[
                "Add Note",
                "List Notes",
                "Update Note",
                "Delete Note",
                "Logout / Exit"
            ],
        ).ask()

        if choice == "Add Note":
            add_note()
        elif choice == "List Notes":
            list_notes()
        elif choice == "Update Note":
            update_note()
        elif choice == "Delete Note":
            delete_note()
        elif choice == "Logout / Exit":
            print("Goodbye!")
            break


def main():
    print("Note Manager")
    while True:
        action = questionary.select(
            "Login or Register?",
            choices=["Login", "Register", "Exit"]
        ).ask()
        if action == "Register":
            register()
        elif action == "Login":
            if login():
                main_menu()
        elif action == "Exit":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()