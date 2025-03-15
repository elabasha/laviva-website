document.addEventListener('DOMContentLoaded', function() {
    let currentIndex = 0;
    const boxes = document.querySelectorAll('.carousel .box');
    const totalBoxes = boxes.length;

    // Make sure there are boxes
    if (totalBoxes === 0) {
        console.error('No boxes found!');
        return;
    }

    // Set initial index to 0
    currentIndex = 0; // The carousel starts at index 0

    function updateCarousel() {
        const carouselInner = document.querySelector('.carousel-inner');
        console.log(`Updating carousel: index=${currentIndex}`);
        // Ensure we're correctly translating the carousel-inner element
        carouselInner.style.transform = `translateX(-${currentIndex * 100}%)`;
    }

    function nextBox() {
        currentIndex = (currentIndex + 1) % totalBoxes; // Loop back to start
        updateCarousel();
    }

    function prevBox() {
        currentIndex = (currentIndex - 1 + totalBoxes) % totalBoxes; // Loop back to the end
        updateCarousel();
    }

    // Attach event listeners for buttons
    const leftArrow = document.querySelector('.arrow.left');
    const rightArrow = document.querySelector('.arrow.right');

    if (leftArrow && rightArrow) {
        leftArrow.addEventListener('click', prevBox);
        rightArrow.addEventListener('click', nextBox);
    } else {
        console.error('Arrow buttons not found!');
    }

    // Initial update to show the carousel at the starting index (0)
    updateCarousel(); // Initial update
});
