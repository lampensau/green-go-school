window.onload = function () {
  let carouselContainer = document.querySelector('.carousel-container');
  let images = carouselContainer.getElementsByTagName('img');
  let captions = carouselContainer.getElementsByTagName('figcaption');
  let currentIndex = 0;

  // Find the image with active image
  for (let i = 0; i < images.length; i++) {
    if (images[i].getAttribute('data-active-image') === 'true') {
      currentIndex = i;
      break;
    }
  }

  function updateActiveImage(index) {
    // Remove active attribute from current image
    images[currentIndex].removeAttribute('data-active-image');
    // Hide corresponding caption
    captions[currentIndex].style.display = 'none';

    // Remove all control hiding classes
    carouselContainer.classList.remove('no-next', 'no-prev');

    // Set the new active image
    images[index].setAttribute('data-active-image', 'true');
    // Show corresponding caption
    captions[index].style.display = 'block';

    // Hide control if we're at the start or the end
    if (index === 0) {
      carouselContainer.classList.add('no-prev');
    }
    if (index === images.length - 1) {
      carouselContainer.classList.add('no-next');
    }

    // Update current index
    currentIndex = index;
  }

  // Create a pseudo button click listener
  function onPseudoButtonClick(event) {
    let rect = carouselContainer.getBoundingClientRect();
    let isPrev = event.clientX < rect.left + rect.width / 2;

    if ((isPrev && currentIndex === 0) || (!isPrev && currentIndex === images.length - 1)) {
      // Don't wrap around
      return;
    }

    let newIndex = isPrev ? currentIndex - 1 : currentIndex + 1;
    updateActiveImage(newIndex);
  }

  carouselContainer.addEventListener('click', onPseudoButtonClick);

  // Initialize first active image and caption
  updateActiveImage(currentIndex);
};
