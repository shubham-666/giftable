# Student Management

A responsive student directory with create, read, update, and delete operations.

## Run

Open `index.html` in a modern browser. No packages, build step, or server are required.

## Features

- Add, edit, search, and delete student records.
- Validate required fields, email addresses, study year, and unique student IDs.
- View live totals for student status and represented courses.
- Keep records in this browser using `localStorage`.
- Adapt the directory and editor for mobile and desktop screens.

Data stays in the browser used to open the app; it is not shared with other devices.

## Publish as its own GitHub repository

Create an empty GitHub repository named `student-management`, then run these commands from this folder:

```powershell
git remote add origin https://github.com/YOUR-USERNAME/student-management.git
git add .
git commit -m "Build student management CRUD app"
git push -u origin main
```
