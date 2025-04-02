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
