"use strict";

const config = {
  label: "student",
  plural: "students",
  storageKey: "campus-desk-students-v1",
  columns: ["name", "studentId", "course", "year", "status"],
  fields: [
    { key: "name", label: "Full name", placeholder: "e.g. Maya Patel", required: true },
    { key: "studentId", label: "Student ID", placeholder: "e.g. STU-1042", required: true },
    { key: "course", label: "Course", type: "select", options: ["Computer Science", "Business", "Design", "Engineering", "Other"] },
    { key: "year", label: "Year of study", type: "number", min: 1, max: 6, required: true },
    { key: "email", label: "Email address", type: "email", placeholder: "student@example.com", required: true },
    { key: "status", label: "Status", type: "select", options: ["Active", "Completed", "Inactive"] },
  ],
  seed: [
    { id: "s-1", name: "Maya Patel", studentId: "STU-1042", course: "Computer Science", year: 2, email: "maya.patel@example.com", status: "Active" },
    { id: "s-2", name: "Ethan Chen", studentId: "STU-1038", course: "Design", year: 3, email: "ethan.chen@example.com", status: "Active" },
    { id: "s-3", name: "Olivia Smith", studentId: "STU-1019", course: "Business", year: 4, email: "olivia.smith@example.com", status: "Completed" },
  ],
  stats: [
    { label: "Total students", icon: "♧", value: (items) => items.length },
    { label: "Active students", icon: "✓", value: (items) => items.filter((item) => item.status === "Active").length },
    { label: "Courses represented", icon: "▤", value: (items) => new Set(items.map((item) => item.course)).size },
    { label: "Completed", icon: "◎", value: (items) => items.filter((item) => item.status === "Completed").length },
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
    console.error("Could not load student records.", error);
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
    console.error("Could not save student records.", error);
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
      if (key === "name") {
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
        cell.textContent = key === "year" ? `Year ${value}` : value;
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
    edit.setAttribute("aria-label", `Edit ${record.name}`);
    const remove = document.createElement("button");
    remove.type = "button";
    remove.className = "action-button delete";
    remove.dataset.action = "delete";
    remove.dataset.id = record.id;
    remove.textContent = "Delete";
    remove.setAttribute("aria-label", `Delete ${record.name}`);
    actionGroup.append(edit, remove);
    actions.append(actionGroup);
    row.append(actions);
    tableBody.append(row);
  }

  document.querySelector("#record-count").textContent = `${visible.length} ${config.plural}`;
  document.querySelector("#empty-title").textContent = records.length ? "No matching students" : "No students yet";
  document.querySelector("#empty-message").textContent = records.length ? "Try a different search term." : "Add a student to get started.";
  document.querySelector("#empty-state").hidden = visible.length > 0;
  tableBody.closest("table").hidden = visible.length === 0;
  renderStats();
}

function buildForm() {
  for (const field of config.fields) {
    const wrapper = document.createElement("div");
    wrapper.className = `field${field.key === "email" ? " full-width" : ""}`;
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
    form.elements[field.key].value = record?.[field.key] ?? config.fields.find((item) => item.key === field.key)?.options?.[0] ?? "";
  }
  document.querySelector("#dialog-title").textContent = editingId ? "Edit student" : "Add student";
  document.querySelector("#save-record").textContent = editingId ? "Save changes" : "Save student";
  dialog.showModal();
  form.elements[editingId ? config.fields[0].key : "name"].focus();
}

document.querySelector("#table-head").append(Object.assign(document.createElement("tr")));
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

  const record = { id: editingId || (globalThis.crypto?.randomUUID?.() ?? `student-${Date.now()}`) };
  for (const field of config.fields) {
    const value = form.elements[field.key].value.trim();
    record[field.key] = field.type === "number" ? Number(value) : value;
  }
  const duplicateId = records.some((item) => item.studentId.toLocaleLowerCase() === record.studentId.toLocaleLowerCase() && item.id !== editingId);
  if (duplicateId) {
    form.elements.studentId.setCustomValidity("This student ID is already in use.");
    form.elements.studentId.reportValidity();
    form.elements.studentId.addEventListener("input", () => form.elements.studentId.setCustomValidity(""), { once: true });
    return;
  }

  const nextRecords = editingId
    ? records.map((item) => item.id === editingId ? record : item)
    : [record, ...records];
  if (saveRecords(nextRecords)) {
    renderTable();
    dialog.close();
    showToast(editingId ? "Student record updated." : "Student added.");
  }
});

tableBody.addEventListener("click", (event) => {
  const button = event.target.closest("button[data-action]");
  if (!button) return;
  const record = records.find((item) => item.id === button.dataset.id);
  if (!record) return;
  if (button.dataset.action === "edit") openDialog(record);
  if (button.dataset.action === "delete" && window.confirm(`Delete ${record.name}'s student record?`)) {
    if (saveRecords(records.filter((item) => item.id !== record.id))) {
      renderTable();
      showToast("Student record deleted.");
    }
  }
});
