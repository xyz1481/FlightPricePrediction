// Add any interactive elements if needed
document.addEventListener("DOMContentLoaded", function () {
  // Add nice focus effects to form elements
  const inputs = document.querySelectorAll("input, select");
  inputs.forEach((input) => {
    input.addEventListener("focus", () => {
      input.parentElement.classList.add("ring-2", "ring-blue-200");
    });
    input.addEventListener("blur", () => {
      input.parentElement.classList.remove("ring-2", "ring-blue-200");
    });
  });

  // Add loading animation to submit button
  const form = document.querySelector("form");
  if (form) {
    form.addEventListener("submit", () => {
      const button = form.querySelector('button[type="submit"]');
      if (button) {
        button.innerHTML =
          '<i class="fas fa-spinner fa-spin mr-2"></i> Predicting...';
        button.disabled = true;
      }
    });
  }
});
