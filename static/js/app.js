document.addEventListener("DOMContentLoaded", () => {
  // Automatically dismiss success messages after a short delay.
  document.querySelectorAll(".message").forEach((message) => {
    window.setTimeout(() => {
      message.style.transition = "opacity .35s ease";
      message.style.opacity = "0";
      window.setTimeout(() => message.remove(), 400);
    }, 3500);
  });
});
