const toggleBtn = document.getElementById("sidebarToggle");
const mobileSidebar = document.getElementById("sidebarOverlay");
const collapseBtn = document.querySelector(".toggle-sidebar");

toggleBtn?.addEventListener("click", () => {
mobileSidebar.classList.toggle("d-none");
});

collapseBtn?.addEventListener("click", () => {
  mobileSidebar?.classList.toggle("collapsed");
});

// Optional: close sidebar when clicking outside
window.addEventListener("click", (e) => {
if (
    mobileSidebar &&
    !mobileSidebar.classList.contains("d-none") &&
    !mobileSidebar.contains(e.target) &&
    e.target !== toggleBtn
) {
    mobileSidebar.classList.add("d-none");
}
});
