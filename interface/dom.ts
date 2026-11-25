// ===== TOP BAR =====
const roundLabelEl = document.getElementById('round-label');
const timerValueEl = document.getElementById('timer-value');
const timerBarEl = document.getElementById('timer-bar');
const playerScoreEl = document.getElementById('player-score');
const computerScoreEl = document.getElementById('computer-score');

// ===== PLAYER CARD =====
const playerCardEl = document.getElementById('player-card');
const playerChoiceEmojiEl = document.getElementById('player-choice-emoji');
const playerChoiceLabelEl = document.getElementById('player-choice-label');
const playerStatusEl = document.getElementById('player-status');

// Player's 3 buttons - R, P, S
const playerButtons = document.querySelectorAll('#player-card .opt');
const playerRockBtn = document.querySelector('#player-card .opt[data-move="R"]');
const playerPaperBtn = document.querySelector('#player-card .opt[data-move="P"]');
const playerScissorsBtn = document.querySelector('#player-card .opt[data-move="S"]');

// ===== COMPUTER CARD =====
const computerCardEl = document.getElementById('computer-card');
const computerChoiceEmojiEl = document.getElementById('computer-choice-emoji');
const computerChoiceLabelEl = document.getElementById('computer-choice-label');
const computerStatusEl = document.getElementById('computer-status');

// Computer's 3 buttons - display only
const computerButtons = document.querySelectorAll('#computer-card .opt');
const computerRockBtn = document.querySelector('#computer-card .opt[data-move="R"]');
const computerPaperBtn = document.querySelector('#computer-card .opt[data-move="P"]');
const computerScissorsBtn = document.querySelector('#computer-card .opt[data-move="S"]');

// ===== RESULT + ACTIONS =====
const resultTextEl = document.getElementById('result-text');
const confirmBtn = document.getElementById('confirm-btn');
const resetBtn = document.getElementById('reset-btn');

// ===== HISTORY =====
const historyListEl = document.getElementById('history-list');