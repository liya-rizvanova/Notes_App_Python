# note_manager.py

import json
from datetime import datetime
from note import Note

class NoteManager:
    def __init__(self, filename='notes.json'):
        self.filename = filename
        self.notes = self.load_notes()
        self.note_counter = len(self.notes) + 1

    def load_notes(self):
        try:
            with open(self.filename, 'r') as file:
                notes_data = json.load(file)
                notes = [Note(**note_data) for note_data in notes_data]
                return notes
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_notes(self):
        notes_data = [{'note_id': note.note_id,
                       'title': note.title,
                       'body': note.body,
                       'created_at': note.created_at,
                       'updated_at': note.updated_at}
                      for note in self.notes]
        with open(self.filename, 'w') as file:
            json.dump(notes_data, file, indent=2)

    def create_note(self, title, body):
        note_id = self.note_counter
        created_at = updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_note = Note(note_id, title, body, created_at, updated_at)
        self.notes.append(new_note)
        self.note_counter += 1
        self.save_notes()

    def display_notes(self):
        for note in self.notes:
            print(f"{note.note_id}. {note.title} - {note.created_at}")

    def view_note(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                print(f"ID: {note.note_id}\nTitle: {note.title}\nBody: {note.body}\nCreated at: {note.created_at}\nUpdated at: {note.updated_at}")
                return
        print(f"Note with ID {note_id} not found.")

    def edit_note(self, note_id, title, body):
        for note in self.notes:
            if note.note_id == note_id:
                note.title = title
                note.body = body
                note.updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.save_notes()
                print(f"Note {note_id} updated successfully.")
                return
        print(f"Note with ID {note_id} not found.")

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note.note_id != note_id]
        self.save_notes()
        print(f"Note {note_id} deleted successfully.")

    def filter_notes_by_date(self, date_str):
        try:
            selected_date = datetime.strptime(date_str, '%Y-%m-%d').strftime('%Y-%m-%d')
            filtered_notes = [note for note in self.notes if note.created_at.startswith(selected_date)]
            
            if filtered_notes:
                for note in filtered_notes:
                    print(f"{note.note_id}. {note.title} - {note.created_at}")
            else:
                print(f"No notes found for {date_str}.")
        except ValueError:
            print("Invalid date format. Please use 'YYYY-MM-DD'.")
