# app.py

from note_manager import NoteManager

def main():
    note_manager = NoteManager()

    while True:
        print("\n1. Display Notes\n2. View Note\n3. Create Note\n4. Edit Note\n5. Delete Note\n6. Filter Notes by Date\n0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            note_manager.display_notes()
        elif choice == '2':
            note_manager.display_notes()
            note_id = int(input("Enter note ID: "))
            note_manager.view_note(note_id)
        elif choice == '3':
            title = input("Enter note title: ")
            body = input("Enter note body: ")
            note_manager.create_note(title, body)
        elif choice == '4':
            note_manager.display_notes()
            note_id = int(input("Enter note ID to edit: "))
            title = input("Enter new title: ")
            body = input("Enter new body: ")
            note_manager.edit_note(note_id, title, body)
        elif choice == '5':
            note_manager.display_notes()
            note_id = int(input("Enter note ID to delete: "))
            note_manager.delete_note(note_id)
        elif choice == '6':
            date_str = input("Enter date (YYYY-MM-DD): ")
            note_manager.filter_notes_by_date(date_str)
        elif choice == '0':
            print("See you!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
