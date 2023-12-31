
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



document.addEventListener('DOMContentLoaded', function () {
    // Set up an IntersectionObserver
    var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                // Trigger smooth scrolling
                var scroll = new SmoothScroll();
                scroll.animateScroll(entry.target);
            }
        });
    }, { threshold: 5.9 }); // Adjust the threshold as needed

    // Observe the entire page
    observer.observe(document.documentElement);
});


document.addEventListener('DOMContentLoaded', function() {
    AOS.init({
        duration: 1200,
        easing: 'ease-in-out',
        once: true,
    });
});


// document.addEventListener('DOMContentLoaded', function () {
//     var mySwiper = new Swiper('.swiper-container', {
//         slidesPerView: 1,
//         spaceBetween: 10,
//         loop: true,
//         autoplay: {
//             delay: 3000,
//             disableOnInteraction: false,
//         },
//     });
// });



 // JavaScript for Scroll-to-Top Button
 const scrollToTopButton = document.getElementById('scroll-to-top');

 // Function to scroll to the top of the page
 function scrollToTop() {window.scrollTo({ top: 0, behavior: 'smooth' });}
 
 // Add click event listener to the button
 scrollToTopButton.addEventListener('click', scrollToTop);
 






const smoothScroll = window;
let lastScrollPosition = window.scrollY;

function smoothScrollTo(destination, duration) {
    const start = window.scrollY;
    const startTime = performance.now();

    function scrollStep(timestamp) {
        const currentTime = timestamp || performance.now();
        const progress = Math.min((currentTime - startTime) / duration, 1);

        window.scrollTo(0, start + progress * (destination - start));

        if (progress < 1) {
            requestAnimationFrame(scrollStep);
        }
    }

    requestAnimationFrame(scrollStep);
}

smoothScroll.addEventListener('scroll', function() {
    const currentScrollPosition = window.scrollY;
    const scrollDirection = currentScrollPosition > lastScrollPosition ? 'down' : 'up';

    lastScrollPosition = currentScrollPosition;
    const destination = scrollDirection === 'down' ? currentScrollPosition + window.innerHeight : currentScrollPosition - window.innerHeight;

    // Call the custom smoothScrollTo function with the desired duration
    smoothScrollTo(destination, 500); // Adjust the duration as needed
});









const longText = [
    "Effortless candidate access, save time, and expand your talent pool with ease.",
    "Swift, efficient hiring, so you focus on building your dream team.",
    "Robust data security ensures your information is always safe and protected.",
    "User-friendly interface for easy profile creation and seamless login.",
    "Structured user management simplifies admin tasks and user interactions.",
];

const delay = 50; // Delay between each character in milliseconds
const typewriterText = document.getElementById("typewriter_text");

function typeWriter(lineIndex, charIndex) {
    if (lineIndex < longText.length) {
        const line = longText[lineIndex];
        if (charIndex < line.length) {
            typewriterText.style.color = "white"
            typewriterText.innerHTML += line.charAt(charIndex);
            charIndex++;
            setTimeout(() => {
                typeWriter(lineIndex, charIndex);
            }, delay);
        } else {
            // Move to the next line
            lineIndex++;
            charIndex = 0;
            setTimeout(() => {
                typewriterText.innerHTML += "<br>"; // Add a line break
                typeWriter(lineIndex, charIndex);
            }, 80); // Pause for 80 miliseconds before starting the next line
        }
    } else {
        // Clear the screen and restart the animation
        setTimeout(() => {
            typewriterText.innerHTML = "";
            typeWriter(0, 0); // Start from the beginning
        }, 1000); // Pause for 1 seconds before restarting
    }
}

let lineIndex = 0; // Initialize line index
let charIndex = 0; // Initialize character index
typeWriter(i, j);