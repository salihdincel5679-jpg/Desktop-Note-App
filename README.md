# 📝 Note App

A simple desktop note-taking application built with Python and Tkinter.

## Features

- Create new notes with a title and content
- Save notes to a local JSON file
- Open and edit existing notes
- Delete notes
- Browse all notes from a dropdown list

## Requirements

- Python 3.x
- Tkinter (comes built-in with Python)
- No external libraries needed

## How to Run

```bash
python main.py
```

## How to Use

| Button | Action |
|--------|--------|
| ☰ | Open the note list |
| New Note | Clear the screen for a new note |
| Save Note | Save the current note |
| Delete Note | Delete the current note |

1. Click **New Note** to start writing
2. Enter a title in the title field
3. Write your note in the text area
4. Click **Save Note** to save

## Project Structure

```
Note App/
│
├── main.py         # Main application file
└── notes.json      # Notes storage file (auto-created on first save)
```

## Data Storage

Notes are stored in a local `notes.json` file in the following format:

```json
{
    "Notes": [
        {
            "id": "unique-uuid",
            "name": "Note Title",
            "content": "Note content here..."
        }
    ]
}
```

## Author

Built as a Python / Tkinter learning project.
