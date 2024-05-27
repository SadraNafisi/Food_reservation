document.getElementById('plusBtn').addEventListener('click', function() {
  let currentValue = parseInt(document.getElementById('numberInput').textContent);
  document.getElementById('numberInput').textContent = currentValue + 1;
  document.querySelector('input[type="hidden"]').value = currentValue + 1;
});

document.getElementById('minusBtn').addEventListener('click', function() {
  let currentValue = parseInt(document.getElementById('numberInput').textContent);
  if (currentValue > 0) {
    document.getElementById('numberInput').textContent = currentValue - 1;
    document.querySelector('input[type="hidden"]').value = currentValue - 1;
  }
});