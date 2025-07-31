const toggleBtn = document.getElementById("sidebarToggle");
const mobileSidebar = document.getElementById("sidebarOverlay");

toggleBtn?.addEventListener("click", () => {
mobileSidebar.classList.toggle("d-none");
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
