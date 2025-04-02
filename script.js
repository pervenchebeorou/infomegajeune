const swiper = new Swiper('.swiper', {
    loop: true, // Permet de faire défiler de manière infinie
    pagination: { 
        el: '.swiper-pagination', // Pagination sous forme de points
        clickable: true 
    },
    navigation: { 
        nextEl: '.swiper-button-next', // Bouton suivant
        prevEl: '.swiper-button-prev'  // Bouton précédent
    }
});


// Fonction pour ouvrir l'image en plein écran
function openFullscreen(img) {
    const overlay = document.getElementById('fullscreenOverlay');
    const fullscreenImage = document.getElementById('fullscreenImage');
    
    fullscreenImage.src = img.src; // Affiche l'image sélectionnée
    overlay.style.display = 'flex'; // Affiche l'overlay
}

// Fonction pour fermer l'overlay
function closeFullscreen() {
    document.getElementById('fullscreenOverlay').style.display = 'none';
}
