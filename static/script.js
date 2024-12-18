const API_URL = '/api/words';

function showModal() {
  document.getElementById('modal').style.display = 'flex';
}

function closeModal() {
  document.getElementById('modal').style.display = 'none';
}

// Lấy từ vựng từ API
async function loadWords() {
  const response = await fetch(API_URL);
  const words = await response.json();

  const wordList = document.getElementById('word-list');
  wordList.innerHTML = '';

  words.forEach((word) => {
    const wordCard = document.createElement('div');
    wordCard.classList.add('word-card');
    wordCard.innerHTML = `
      <img src="/static/images/${word.image}" alt="${word.text}" class="word-image">
      <p>${word.text}</p>
      <button class="speak-button" data-word="${word.text}">Nghe phát âm</button>
    `;
    wordList.appendChild(wordCard);
  });

  // Thêm sự kiện cho nút phát âm
  document.querySelectorAll('.speak-button').forEach((button) => {
    button.addEventListener('click', () => {
      const word = button.getAttribute('data-word');
      speakWord(word);
    });
  });
}

// Hàm phát âm
function speakWord(word) {
  const utterance = new SpeechSynthesisUtterance(word);
  utterance.lang = 'vi-VN';  // Đặt ngôn ngữ tiếng Việt
  window.speechSynthesis.speak(utterance);
}
function showModal() {
  document.getElementById('modal').style.display = 'flex';
}

function closeModal() {
  document.getElementById('modal').style.display = 'none';
}

// Tải từ vựng khi trang load
loadWords();
