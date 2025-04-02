const swiper = new Swiper('.swiper', {
    loop: true,
    pagination: { el: '.swiper-pagination', clickable: true },
    navigation: { nextEl: '.swiper-button-next', prevEl: '.swiper-button-prev' },
});

function openFullscreen(img) {
    const overlay = document.getElementById('fullscreenOverlay');
    const fullscreenImage = document.getElementById('fullscreenImage');
    
    fullscreenImage.src = img.src; 
    overlay.style.display = 'flex'; 
}

function closeFullscreen() {
    document.getElementById('fullscreenOverlay').style.display = 'none';
}
