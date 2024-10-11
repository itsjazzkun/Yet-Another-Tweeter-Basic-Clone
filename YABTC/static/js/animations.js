// animations.js

// Add a fade-in effect to elements when the page loads
document.addEventListener('DOMContentLoaded', function() {
    const elements = document.querySelectorAll('.fade-in');
    elements.forEach(element => {
        element.classList.add('opacity-0', 'transition-opacity', 'duration-1000');
        setTimeout(() => {
            element.classList.remove('opacity-0');
            element.classList.add('opacity-100');
        }, 100);
    });
});

// Smooth scrolling for internal links
const scrollLinks = document.querySelectorAll('a[href^="#"]');
scrollLinks.forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        const target = document.querySelector(targetId);
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start',
            });
        }
    });
});

// Add a hover animation for buttons
const buttons = document.querySelectorAll('.hover-effect');
buttons.forEach(button => {
    button.addEventListener('mouseenter', () => {
        button.classList.add('scale-105');
    });
    button.addEventListener('mouseleave', () => {
        button.classList.remove('scale-105');
    });
});
