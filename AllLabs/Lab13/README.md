# Lab13 — Resume and Mini Library webpages

This folder contains the two webpages for the class:

- `index.html` — Shubham Tiwari's resume
- `projects.html` — an explanation of the Python Mini Library System, including a working browser demo
- `script.js` — the demo's add, borrow, and return behavior
- `style.css` — the shared responsive page styling

Open `index.html` in a browser. Use the navigation links to move between the resume and the library project page. `projects.html` can add titles, merge copies for a matching title, borrow only when copies are available, and return a copy. Refreshing the page clears the demo list; the separate Python program saves its library data to JSON and exports CSV.

The resume includes the supplied name, email, GitHub profile, education, current skills, and project descriptions. The browser demo uses text-only DOM updates for book titles and author names, so entered text is displayed as text instead of being interpreted as HTML.

## Publish with GitHub Pages

Commit and push these files first. In the repository's GitHub settings, open **Pages** and choose the `main` branch with the repository root as the publishing source. After GitHub Pages finishes publishing, these pages will be available at:

- `https://shubham-666.github.io/giftable/AllLabs/Lab13/`
- `https://shubham-666.github.io/giftable/AllLabs/Lab13/projects.html`

The links work after Pages is enabled for the repository and these changes are pushed to `main`.

## Before class

- Open both pages in a browser and use the navigation links.
- On the Library page, add a book, add that title again with different capitalization, borrow until no copies remain, and try borrowing once more.
- Narrow the browser window to check the responsive layout.
- Be ready to explain the page structure in HTML, the styling in `style.css`, and the event handlers and rendering functions in `script.js`.
