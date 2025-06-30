document.getElementById("upload-form").addEventListener("submit", async (e) => {
  e.preventDefault();

  const audioInput = document.getElementById("audio-file");
  const file = audioInput.files[0];
  const transcribeBtn = document.getElementById("transcribe-btn");

  if (!file) {
    alert("Please select an audio file.");
    return;
  }

  const formData = new FormData();
  formData.append("audio", file);

  transcribeBtn.textContent = "Processing...";
  transcribeBtn.disabled = true;

  try {
    const response = await fetch("/upload", {
      method: "POST",
      body: formData,
    });

    const result = await response.json();
    document.getElementById("transcription-text").textContent = result.text;
    transcribeBtn.textContent = "Transcribed";
    transcribeBtn.disabled = true; // make unclickable
  } catch (err) {
    document.getElementById("transcription-text").textContent =
      "⚠️ Error during transcription.";
    console.error("Transcription error:", err);
    transcribeBtn.textContent = "Transcribe";
    transcribeBtn.disabled = false;
  }
});

document.getElementById("clear-btn").addEventListener("click", () => {
  document.getElementById("audio-file").value = "";
  document.getElementById("transcription-text").textContent =
    "Your transcription will appear here...";
  const transcribeBtn = document.getElementById("transcribe-btn");
  transcribeBtn.textContent = "Transcribe";
  transcribeBtn.disabled = false;
});
