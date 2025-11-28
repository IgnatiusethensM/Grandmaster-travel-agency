class Carousel {
    constructor(container) {
        this.container = container;
        this.track = container.querySelector('.carousel-track');
        this.items = container.querySelectorAll('.carousel-item');
        this.prevBtn = container.querySelector('.carousel-prev');
        this.nextBtn = container.querySelector('.carousel-next');
        this.dots = container.querySelectorAll('.dot');

        this.currentIndex = 0;
        this.itemsPerView = this.getItemsPerView();
        this.maxIndex = Math.max(0, this.items.length - this.itemsPerView);

        this.init();
    }

    getItemsPerView() {
        if (window.innerWidth >= 1024) return 3;
        if (window.innerWidth >= 768) return 2;
        return 1;
    }

    init() {
        this.prevBtn?.addEventListener('click', () => this.prev());
        this.nextBtn?.addEventListener('click', () => this.next());

        this.dots.forEach((dot, index) => {
            dot.addEventListener('click', () => this.goTo(index));
        });

        window.addEventListener('resize', () => {
            this.itemsPerView = this.getItemsPerView();
            this.maxIndex = Math.max(0, this.items.length - this.itemsPerView);
            this.goTo(Math.min(this.currentIndex, this.maxIndex));
        });

        // Auto-advance every 5 seconds
        this.autoPlay = setInterval(() => this.next(), 5000);

        // Pause on hover
        this.container.addEventListener('mouseenter', () => clearInterval(this.autoPlay));
        this.container.addEventListener('mouseleave', () => {
            this.autoPlay = setInterval(() => this.next(), 5000);
        });

        this.updateButtons();
    }

    next() {
        if (this.currentIndex < this.maxIndex) {
            this.goTo(this.currentIndex + 1);
        } else {
            this.goTo(0); // Loop back
        }
    }

    prev() {
        if (this.currentIndex > 0) {
            this.goTo(this.currentIndex - 1);
        } else {
            this.goTo(this.maxIndex); // Loop to end
        }
    }

    goTo(index) {
        this.currentIndex = Math.max(0, Math.min(index, this.maxIndex));
        const offset = (this.currentIndex / this.items.length) * 100;
        this.track.style.transform = `translateX(-${offset}%)`;
        this.updateDots();
        this.updateButtons();
    }

    updateDots() {
        this.dots.forEach((dot, index) => {
            dot.classList.toggle('bg-white', index === this.currentIndex);
            dot.classList.toggle('bg-white/50', index !== this.currentIndex);
        });
    }

    updateButtons() {
        if (this.prevBtn) {
            this.prevBtn.disabled = this.currentIndex === 0;
            this.prevBtn.style.opacity = this.currentIndex === 0 ? '0.5' : '1';
        }
        if (this.nextBtn) {
            this.nextBtn.disabled = this.currentIndex === this.maxIndex;
            this.nextBtn.style.opacity = this.currentIndex === this.maxIndex ? '0.5' : '1';
        }
    }
}

// Initialize carousels
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('[id$="Carousel"]').forEach(container => {
        new Carousel(container);
    });
});
