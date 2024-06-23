document.addEventListener("DOMContentLoaded", function() {
  const subscribeModal = document.getElementById('subscribeModal');
  const openButton = document.getElementById('openSubscribeModal');
  const closeButton = document.getElementById('closeSubscribeModal');
  const closeSubscribeModal = () => {
    subscribeModal.style.display = "none";
  }

  openButton.onclick = () => {subscribeModal.style.display = "block"};
  closeButton.onclick = closeSubscribeModal;

  // Clicking outside of the modal
  window.onclick = function(event) {
    if (event.target == document.getElementById('subscribeModal')) {
      closeSubscribeModal();
    }
  }

  document.addEventListener('keydown', function(event) {
    if (event.key === "Escape") {
      closeSubscribeModal();
    }
  });
});