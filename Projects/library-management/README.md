# Library Management

A responsive library inventory with create, read, update, and delete operations.

## Run

Open `index.html` in a modern browser. No packages, build step, or server are required.

## Features

- Add, edit, search, and delete book records.
- Validate required details, copy counts, and unique book titles.
- View live title, copy, availability, and category totals.
- Keep records in this browser using `localStorage`.
- Adapt the inventory and editor for mobile and desktop screens.

Data stays in the browser used to open the app; it is not shared with other devices.

## Publish as its own GitHub repository

Create an empty GitHub repository named `library-management`, then run these commands from this folder:

```powershell
git remote add origin https://github.com/YOUR-USERNAME/library-management.git
git add .
git commit -m "Build library management CRUD app"
git push -u origin main
```
