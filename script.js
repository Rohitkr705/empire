window.onload = function() {
    let navbar = document.querySelector('.navbar');
    document.querySelector('#menu-btn').onclick = function() {
        navbar.classList.toggle('active');
    };
};
