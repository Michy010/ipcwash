let menuVisible = false; // Variable to track menu visibility

function toggleMenu() {
    var navbar = document.getElementById("navbar");
    var hamburgerIcon = document.querySelector(".menu-toggle");
    
    if (menuVisible) {
        navbar.classList.remove("active");
        hamburgerIcon.style.display = "block"; // Show the hamburger icon again
    } else {
        navbar.classList.add("active");
        hamburgerIcon.style.display = "none"; // Hide the hamburger icon
    }
    menuVisible = !menuVisible;
}