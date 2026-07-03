// Grab references to all the HTML elements we need
const translateBtn = document.getElementById('translateBtn');
const inputText    = document.getElementById('inputText');
const outputText   = document.getElementById('outputText');
const sourceLang   = document.getElementById('sourceLang');
const targetLang   = document.getElementById('targetLang');
const copyBtn      = document.getElementById('copyBtn');
const speakBtn     = document.getElementById('speakBtn');
const swapBtn      = document.getElementById('swapBtn');

// ── TRANSLATE ──────────────────────────────────────────────────────────────
translateBtn.addEventListener('click', async () => {
  const text = inputText.value.trim();

  // Guard: don't call API if input is empty
  if (!text) {
    outputText.textContent = 'Please enter some text first.';
    return;
  }

  outputText.textContent = 'Translating...';

  const from = sourceLang.value;   // e.g. "en"
  const to   = targetLang.value;   // e.g. "hi"

  // Google Translate's unofficial public endpoint — free, no API key needed,
  // and generally gives more accurate translations than MyMemory.
  // client=gtx is the "web client" mode that doesn't require authentication.
  const url = `https://translate.googleapis.com/translate_a/single?client=gtx&sl=${from}&tl=${to}&dt=t&q=${encodeURIComponent(text)}`;

  try {
    const response = await fetch(url);          // send the request
    const data     = await response.json();     // parse the JSON reply

    // Debug: log the full response so we can see exactly what the API sent back
    console.log('API response:', data);

    // Google's response is a nested array. The translated text pieces are at
    // data[0][i][0] for each chunk i. We join them all together in case the
    // sentence was split into multiple chunks.
    const result = data?.[0]?.map(chunk => chunk[0]).join('');

    if (result && result.trim() !== '') {
      outputText.textContent = result;
    } else {
      // API responded, but no usable translation came back
      outputText.textContent = 'Translation failed. Try again or use shorter text.';
      console.warn('No translation found in response:', data);
    }

  } catch (error) {
    // If anything goes wrong (no internet, API down, bad JSON, etc.)
    outputText.textContent = 'Error: Could not translate. Check your connection.';
    console.error(error);
  }
});

// ── SWAP LANGUAGES ─────────────────────────────────────────────────────────
swapBtn.addEventListener('click', () => {
  const temp        = sourceLang.value;
  sourceLang.value  = targetLang.value;
  targetLang.value  = temp;
});

// ── COPY ───────────────────────────────────────────────────────────────────
copyBtn.addEventListener('click', () => {
  const text = outputText.textContent;
  if (!text || text === 'Translation will appear here.') return;

  navigator.clipboard.writeText(text).then(() => {
    copyBtn.textContent = '✅ Copied!';
    setTimeout(() => { copyBtn.textContent = '📋 Copy'; }, 2000);
  });
});

// ── TEXT-TO-SPEECH ─────────────────────────────────────────────────────────

speakBtn.addEventListener('click', () => {
  const text = outputText.textContent;
  if (!text || text === 'Translation will appear here.') return;

  const availableVoices = speechSynthesis.getVoices();
  const targetCode = targetLang.value; // e.g. "hi"

  // Try to find a voice that exactly matches our target language
  const matchedVoice = availableVoices.find(v => v.lang.toLowerCase().startsWith(targetCode.toLowerCase()));

  const utterance = new SpeechSynthesisUtterance(text);

  if (matchedVoice) {
    // Best case: exact language voice found
    utterance.voice = matchedVoice;
    utterance.lang  = matchedVoice.lang;
  } else if (availableVoices.length > 0) {
    // Fallback: no matching voice available right now (often happens with
    // online/Google voices that fail to load). Use the browser's default
    // voice instead of failing silently — pronunciation won't be perfect,
    // but the user gets SOME audio instead of nothing.
    utterance.lang = targetCode;
    console.warn(`No exact voice for "${targetCode}". Using default voice instead.`);
    speakBtn.textContent = '⚠️ Voice unavailable, using default';
    setTimeout(() => { speakBtn.textContent = '🔊 Speak'; }, 2500);
  } else {
    // No voices at all loaded — nothing we can do right now
    speakBtn.textContent = '❌ No voices available';
    setTimeout(() => { speakBtn.textContent = '🔊 Speak'; }, 2500);
    return;
  }

  speechSynthesis.cancel();   // stop any speech already in progress
  speechSynthesis.speak(utterance);
});
