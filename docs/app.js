const config = window.DRONETECH_CONFIG || {};
const apiBaseUrl = (config.API_BASE_URL || "http://localhost:8000").replace(/\/$/, "");

const chat = document.getElementById("chat");
const form = document.getElementById("chat-form");
const input = document.getElementById("message-input");
const roleSelect = document.getElementById("role-select");
const quickButtons = document.querySelectorAll(".quick-actions button");

function addMessage(text, kind, meta = "") {
  const el = document.createElement("div");
  el.className = `message ${kind}`;
  el.textContent = text;
  if (meta) {
    const metaEl = document.createElement("span");
    metaEl.className = "meta";
    metaEl.textContent = meta;
    el.appendChild(document.createElement("br"));
    el.appendChild(metaEl);
  }
  chat.appendChild(el);
  chat.scrollTop = chat.scrollHeight;
}

async function sendMessage(message) {
  addMessage(message, "user");
  input.value = "";
  try {
    const response = await fetch(`${apiBaseUrl}/ask`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        message,
        role: roleSelect.value,
        conversation_id: crypto.randomUUID(),
        language: "nl",
        channel_context: { team_id: "pilot-team", channel_id: "drone-kanaal" }
      })
    });
    const data = await response.json();
    const sourceNames = (data.sources || []).map(s => s.title || s.document).join(" | ");
    const meta = [data.category, data.safety?.escalate ? "escaleren" : null, sourceNames].filter(Boolean).join(" • ");
    addMessage(data.answer || "Geen antwoord ontvangen.", "assistant", meta);
  } catch (error) {
    addMessage(`Fout bij backend: ${error.message}`, "assistant", "technische fout");
  }
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const message = input.value.trim();
  if (!message) return;
  await sendMessage(message);
});

quickButtons.forEach((btn) => {
  btn.addEventListener("click", async () => await sendMessage(btn.dataset.prompt));
});

addMessage("Welkom. Stel een vraag over drone-techniek, checklists, PvE’s, logboeken of examenvluchtvoorbereiding.", "assistant", "start");
