document.addEventListener('DOMContentLoaded', function () {
    // Testimonials Carousel Logic
    const track = document.querySelector('.carousel-track');
    if (track) {
        const items = document.querySelectorAll('.carousel-item');
        const prevBtn = document.querySelector('.carousel-prev');
        const nextBtn = document.querySelector('.carousel-next');
        const dots = document.querySelectorAll('.dot');

        let currentIndex = 0;
        const itemWidth = items[0].offsetWidth;
        const itemsPerView = Math.round(track.offsetWidth / itemWidth);
        const maxIndex = items.length - itemsPerView;

        function updateCarousel() {
            const translateX = -(currentIndex * itemWidth);
            track.style.transform = `translateX(${translateX}px)`;

            // Update dots
            dots.forEach((dot, index) => {
                dot.classList.toggle('bg-white', index === currentIndex);
                dot.classList.toggle('bg-white/50', index !== currentIndex);
            });
        }

        if (prevBtn) {
            prevBtn.addEventListener('click', () => {
                if (currentIndex > 0) {
                    currentIndex--;
                    updateCarousel();
                }
            });
        }

        if (nextBtn) {
            nextBtn.addEventListener('click', () => {
                if (currentIndex < maxIndex) {
                    currentIndex++;
                    updateCarousel();
                }
            });
        }

        dots.forEach((dot, index) => {
            dot.addEventListener('click', () => {
                currentIndex = index;
                // Clamp index
                if (currentIndex > maxIndex) currentIndex = maxIndex;
                updateCarousel();
            });
        });

        // Handle resize
        window.addEventListener('resize', () => {
            // Re-calculate on resize
            const newItemWidth = items[0].offsetWidth;
            const newItemsPerView = Math.round(track.offsetWidth / newItemWidth);
            const newMaxIndex = items.length - newItemsPerView;

            if (currentIndex > newMaxIndex) currentIndex = newMaxIndex;

            const translateX = -(currentIndex * newItemWidth);
            track.style.transform = `translateX(${translateX}px)`;
        });
    }
});
