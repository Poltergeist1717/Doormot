
// Toggle For NavBars
function toggleNavBar() {
    const content_box = document.getElementById('content-box');
    const hamburger = document.getElementById('hamburger');
    const nav_list = document.getElementById('navlist');
    const log_nav_list = document.getElementById('log-nav-list');

    if (window.innerWidth <=768){
        if (content_box.style.display === 'block') {
            // List is currently displayed, retract it
            content_box.style.display = 'none';
            hamburger.innerHTML =  `
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-white" fill="white" viewBox="0 0 24 24" stroke="currentColor" id="hamburger">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>`;
            
        } else {
            // List is hidden, display it
            content_box.style.display = 'block';
            content_box.style.height = '250px';
            nav_list.style.display = 'block';
            log_nav_list.style.display = 'block';
            hamburger.innerHTML = `
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-white" fill="white" viewBox="0 0 24 24" stroke="currentColor" id="hamburger">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>`;
        }
    }
    else {
        content_box.style.display = 'flex';
        nav_list.style.display = 'flex';
        log_nav_list.style.display = 'flex';
        content_box.style.height = 'auto';
    }
}

// Add an event listener to the icon for toggling the navigation bar
const icon = document.getElementById('hamburger');
icon.addEventListener('click', toggleNavBar);
