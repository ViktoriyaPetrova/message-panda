//Check for HTML tags
function escapeHTML(input) {
  return input.replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function handleContextInput() {
  let contextTextarea = document.getElementById('context');
  let maxLength = parseInt(contextTextarea.getAttribute('maxLength'));
  let currentLength = contextTextarea.value.length;
  let inputCount = document.getElementById('contextCount');

  //Sanitize input
  contextTextarea.value = escapeHTML(contextTextarea.value);
  //Check max length and trim if needed
  if (currentLength > maxLength) {
    contextTextarea.value = contextTextarea.value.slice(0, maxLength);
  }
  //Display current and max length
  inputCount.textContent = currentLength + '/' + maxLength + ' characters used';
}

function handleReplyInput() {
  let replyTextarea = document.getElementById('reply');
  let maxLength = parseInt(replyTextarea.getAttribute('maxLength'));
  let currentLength = replyTextarea.value.length;
  let inputCount = document.getElementById('replyCount');

  //Sanitize input
  replyTextarea.value = escapeHTML(replyTextarea.value);
  //Check max length and trim if needed
  if (currentLength > maxLength) {
    replyTextarea.value = replyTextarea.value.slice(0, maxLength);
  }
  //Display current and max length
  inputCount.textContent = currentLength + '/' + maxLength + ' characters used';
}

function handleYesClick() {
  //Query the DOM and save all necessary elements
  let container = document.getElementById('replyContainer');
  // Query the DOM and check if the textarea already exists
  let existingTextarea = document.getElementById('reply');

  // If the textarea already exists, do nothing
  if (existingTextarea) {
    return;
  }

  //Create new DOM elements
  let textarea = document.createElement('textarea');
  let label = document.createElement('label');
  let lineBreak = document.createElement('br');
  let replyCount = document.createElement('span');

  //Set the attributes for the new elements
  label.setAttribute('for', 'reply');
  label.textContent = 'Message you are replying to:';
  textarea.id = 'reply';
  textarea.name = 'reply';
  textarea.className = 'form-control';
  textarea.maxLength = '1000';
  textarea.style.height = '200px';
  textarea.placeholder = 'Paste the message here...';
  textarea.oninput = handleReplyInput;
  replyCount.id = 'replyCount';
  replyCount.textContent = '0/1000 characters used';

  //Add the elements to the DOM
  container.appendChild(label);
  container.appendChild(lineBreak);
  container.appendChild(textarea);
  container.appendChild(replyCount);
}

function handleNoClick() {
  let container = document.getElementById('replyContainer');

  while (container.firstChild) {
    container.removeChild(container.firstChild);
  }
}

function showSpinner() {
  document.getElementById('loading').style.display = 'block';
  response = document.getElementById('response');
  placeholder = document.getElementById('placeholder');

  if (response) response.remove();
  if (placeholder) placeholder.remove();
}
