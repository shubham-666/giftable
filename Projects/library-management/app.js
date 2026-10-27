"use strict";

const config = {
  label: "book",
  plural: "books",
  storageKey: "campus-desk-library-v1",
  columns: ["title", "author", "category", "copies", "status"],
  fields: [
    { key: "title", label: "Book title", placeholder: "e.g. The Design of Everyday Things", required: true },
    { key: "author", label: "Author", placeholder: "e.g. Don Norman", required: true },
    { key: "category", label: "Category", type: "select", options: ["Fiction", "Technology", "Science", "History", "Reference", "Other"] },
    { key: "copies", label: "Total copies", type: "number", min: 1, max: 9999, required: true },
    { key: "status", label: "Availability", type: "select", options: ["Available", "Borrowed"] },
  ],
  seed: [
    { id: "b-1", title: "The Design of Everyday Things", author: "Don Norman", category: "Reference", copies: 12, status: "Available" },
    { id: "b-2", title: "Atomic Habits", author: "James Clear", category: "Science", copies: 8, status: "Available" },
    { id: "b-3", title: "The Great Gatsby", author: "F. Scott Fitzgerald", category: "Fiction", copies: 0, status: "Borrowed" },
  ],
  stats: [
    { label: "Unique titles", icon: "▤", value: (items) => items.length },
    { label: "Total copies", icon: "▦", value: (items) => items.reduce((sum, item) => sum + Number(item.copies || 0), 0) },
    { label: "Available titles", icon: "✓", value: (items) => items.filter((item) => item.status === "Available").length },
    { label: "Categories", icon: "◎", value: (items) => new Set(items.map((item) => item.category)).size },
  ],
};

const form = document.querySelector("#record-form");
const dialog = document.querySelector("#record-dialog");
const fieldsContainer = document.querySelector("#form-fields");
const tableHead = document.querySelector("#table-head");
const tableBody = document.querySelector("#table-body");
const search = document.querySelector("#search");
const toast = document.querySelector("#toast");
let records = [];
let editingId = null;
let toastTimer;

function showToast(message, isError = false) {
  toast.textContent = message;
  toast.classList.toggle("error", isError);
  toast.classList.add("visible");
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => toast.classList.remove("visible"), 3000);
}

function loadRecords() {
  try {
    const saved = localStorage.getItem(config.storageKey);
    if (saved === null) {
      records = config.seed.map((item) => ({ ...item }));
      localStorage.setItem(config.storageKey, JSON.stringify(records));
      return;
    }
    const parsed = JSON.parse(saved);
    if (!Array.isArray(parsed)) throw new Error("Saved records are not a list.");
    records = parsed;
  } catch (error) {
    console.error("Could not load library records.", error);
    records = config.seed.map((item) => ({ ...item }));
    showToast("Could not load saved records. Check browser storage and refresh.", true);
  }
}

function saveRecords(nextRecords) {
  try {
    localStorage.setItem(config.storageKey, JSON.stringify(nextRecords));
    records = nextRecords;
    return true;
  } catch (error) {
    console.error("Could not save library records.", error);
    showToast("Your change could not be saved. Check browser storage and try again.", true);
    return false;
  }
}

function initials(name) {
  return String(name || "?").trim().split(/\s+/).slice(0, 2).map((part) => part[0] || "").join("").toUpperCase();
}

function renderStats() {
  const container = document.querySelector("#stats");
  container.replaceChildren();
  for (const stat of config.stats) {
    const card = document.createElement("article");
    card.className = "stat-card";
    const top = document.createElement("div");
    top.className = "stat-top";
    const label = document.createElement("span");
    label.textContent = stat.label;
    const icon = document.createElement("span");
    icon.className = "stat-icon";
    icon.setAttribute("aria-hidden", "true");
    icon.textContent = stat.icon;
    top.append(label, icon);
    const value = document.createElement("div");
    value.className = "stat-value";
    value.textContent = String(stat.value(records));
    card.append(top, value);
    container.append(card);
  }
}

function renderTable() {
  const query = search.value.trim().toLocaleLowerCase();
  const visible = records.filter((record) => config.fields.some((field) => String(record[field.key] ?? "").toLocaleLowerCase().includes(query)));
  tableBody.replaceChildren();

  for (const record of visible) {
    const row = document.createElement("tr");
    for (const key of config.columns) {
      const cell = document.createElement("td");
      const value = String(record[key] ?? "—");
      if (key === "title") {
        const person = document.createElement("div");
        person.className = "person-cell";
        const avatar = document.createElement("span");
        avatar.className = "row-avatar";
        avatar.setAttribute("aria-hidden", "true");
        avatar.textContent = initials(value);
        const name = document.createElement("span");
        name.textContent = value;
        person.append(avatar, name);
        cell.append(person);
      } else if (key === "status") {
        const badge = document.createElement("span");
        badge.className = `status-badge ${value.toLowerCase().replace(/[^a-z0-9-]/g, "")}`;
        badge.textContent = value;
        cell.append(badge);
      } else {
        cell.textContent = value;
      }
      row.append(cell);
    }

    const actions = document.createElement("td");
    const actionGroup = document.createElement("div");
    actionGroup.className = "row-actions";
    const edit = document.createElement("button");
    edit.type = "button";
    edit.className = "action-button";
    edit.dataset.action = "edit";
    edit.dataset.id = record.id;
    edit.textContent = "Edit";
    edit.setAttribute("aria-label", `Edit ${record.title}`);
    const remove = document.createElement("button");
    remove.type = "button";
    remove.className = "action-button delete";
    remove.dataset.action = "delete";
    remove.dataset.id = record.id;
    remove.textContent = "Delete";
    remove.setAttribute("aria-label", `Delete ${record.title}`);
    actionGroup.append(edit, remove);
    actions.append(actionGroup);
    row.append(actions);
    tableBody.append(row);
  }

  document.querySelector("#record-count").textContent = `${visible.length} ${config.plural}`;
  document.querySelector("#empty-title").textContent = records.length ? "No matching books" : "No books yet";
  document.querySelector("#empty-message").textContent = records.length ? "Try a different search term." : "Add a book to get started.";
  document.querySelector("#empty-state").hidden = visible.length > 0;
  tableBody.closest("table").hidden = visible.length === 0;
  renderStats();
}

function buildForm() {
  for (const field of config.fields) {
    const wrapper = document.createElement("div");
    wrapper.className = `field${field.key === "title" ? " full-width" : ""}`;
    const label = document.createElement("label");
    label.htmlFor = `field-${field.key}`;
    label.textContent = field.label;
    const input = document.createElement(field.type === "select" ? "select" : "input");
    input.id = `field-${field.key}`;
    input.name = field.key;
    input.required = Boolean(field.required);
    if (field.type && field.type !== "select") input.type = field.type;
    if (field.placeholder) input.placeholder = field.placeholder;
    if (field.min !== undefined) input.min = String(field.min);
    if (field.max !== undefined) input.max = String(field.max);
    if (field.options) {
      for (const optionValue of field.options) {
        const option = document.createElement("option");
        option.value = optionValue;
        option.textContent = optionValue;
        input.append(option);
      }
    }
    wrapper.append(label, input);
    fieldsContainer.append(wrapper);
  }
}

function openDialog(record = null) {
  editingId = record?.id ?? null;
  form.reset();
  for (const field of config.fields) {
    form.elements[field.key].value = record?.[field.key] ?? field.options?.[0] ?? "";
  }
  document.querySelector("#dialog-title").textContent = editingId ? "Edit book" : "Add book";
  document.querySelector("#save-record").textContent = editingId ? "Save changes" : "Save book";
  dialog.showModal();
  form.elements.title.focus();
}

tableHead.append(Object.assign(document.createElement("tr")));
for (const key of config.columns) {
  const heading = document.createElement("th");
  heading.scope = "col";
  heading.textContent = config.fields.find((field) => field.key === key).label;
  tableHead.firstElementChild.append(heading);
}
const actionsHeading = document.createElement("th");
actionsHeading.scope = "col";
actionsHeading.textContent = "ACTIONS";
tableHead.firstElementChild.append(actionsHeading);

buildForm();
loadRecords();
renderTable();

document.querySelector("#add-record").addEventListener("click", () => openDialog());
document.querySelector("#close-dialog").addEventListener("click", () => dialog.close());
document.querySelector("#cancel-dialog").addEventListener("click", () => dialog.close());
search.addEventListener("input", renderTable);

form.addEventListener("submit", (event) => {
  event.preventDefault();
  if (!form.reportValidity()) return;

  const record = { id: editingId || (globalThis.crypto?.randomUUID?.() ?? `book-${Date.now()}`) };
  for (const field of config.fields) {
    const value = form.elements[field.key].value.trim();
    record[field.key] = field.type === "number" ? Number(value) : value;
  }
  const duplicateTitle = records.some((item) => item.title.toLocaleLowerCase() === record.title.toLocaleLowerCase() && item.id !== editingId);
  if (duplicateTitle) {
    form.elements.title.setCustomValidity("This book title is already in the collection.");
    form.elements.title.reportValidity();
    form.elements.title.addEventListener("input", () => form.elements.title.setCustomValidity(""), { once: true });
    return;
  }

  const nextRecords = editingId
    ? records.map((item) => item.id === editingId ? record : item)
    : [record, ...records];
  if (saveRecords(nextRecords)) {
    renderTable();
    dialog.close();
    showToast(editingId ? "Book record updated." : "Book added.");
  }
});

tableBody.addEventListener("click", (event) => {
  const button = event.target.closest("button[data-action]");
  if (!button) return;
  const record = records.find((item) => item.id === button.dataset.id);
  if (!record) return;
  if (button.dataset.action === "edit") openDialog(record);
  if (button.dataset.action === "delete" && window.confirm(`Delete "${record.title}" from the collection?`)) {
    if (saveRecords(records.filter((item) => item.id !== record.id))) {
      renderTable();
      showToast("Book deleted.");
    }
  }
});
