"use strict";

const books = [];
const form = document.getElementById("book-form");
const shelf = document.getElementById("book-shelf");
const message = document.getElementById("library-message");
const titleCount = document.getElementById("title-count");
const copyCount = document.getElementById("copy-count");

function findBook(title) {
  const normalizedTitle = title.trim().toLocaleLowerCase();
  return books.find((book) => book.title.toLocaleLowerCase() === normalizedTitle);
}

function showMessage(text) {
  message.textContent = text;
}

function makeButton(label, action) {
  const button = document.createElement("button");
  button.type = "button";
  button.textContent = label;
  button.addEventListener("click", action);
  return button;
}

function renderBooks() {
  shelf.replaceChildren();
  titleCount.textContent = books.length;

  const totalCopies = books.reduce((total, book) => total + book.copies, 0);
  copyCount.textContent = totalCopies;

  if (books.length === 0) {
    const emptyMessage = document.createElement("p");
    emptyMessage.className = "empty-shelf";
    emptyMessage.textContent = "No books yet. Add one above to get started.";
    shelf.appendChild(emptyMessage);
    return;
  }

  for (const book of books) {
    const card = document.createElement("article");
    card.className = "book-card";

    const title = document.createElement("h3");
    title.textContent = book.title;

    const author = document.createElement("p");
    author.className = "book-author";
    author.textContent = `by ${book.author}`;

    const count = document.createElement("p");
    count.className = "book-count";
    count.textContent = `${book.copies} available`;

    const actions = document.createElement("div");
    actions.className = "book-actions";
    actions.append(
      makeButton("Borrow", () => borrowBook(book)),
      makeButton("Return", () => returnBook(book))
    );

    card.append(title, author, count, actions);
    shelf.appendChild(card);
  }
}

function borrowBook(book) {
  if (book.copies === 0) {
    showMessage(`No copies of "${book.title}" are available to borrow.`);
    return;
  }

  book.copies -= 1;
  showMessage(`Borrowed "${book.title}".`);
  renderBooks();
}

function returnBook(book) {
  book.copies += 1;
  showMessage(`Returned "${book.title}".`);
  renderBooks();
}

form.addEventListener("submit", (event) => {
  event.preventDefault();

  const titleInput = document.getElementById("book-title");
  const authorInput = document.getElementById("book-author");
  const copiesInput = document.getElementById("book-copies");
  const title = titleInput.value.trim();
  const author = authorInput.value.trim();
  const copies = Number(copiesInput.value);

  if (!title || !author || !Number.isInteger(copies) || copies < 1) {
    showMessage("Enter a title, an author, and a whole number of copies greater than zero.");
    return;
  }

  const existingBook = findBook(title);
  if (existingBook) {
    existingBook.copies += copies;
    showMessage(`Added ${copies} more ${copies === 1 ? "copy" : "copies"} of "${existingBook.title}".`);
  } else {
    books.push({ title, author, copies });
    showMessage(`Added "${title}" to the library.`);
  }

  form.reset();
  copiesInput.value = "1";
  renderBooks();
});

renderBooks();
