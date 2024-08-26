console.log("Checking JavaScript - bio modal")

// Control the teacher bio modal
const modalBio = document.getElementById('modal-bio');
const bioTrigger = document.getElementById('bio-modal-trigger');
const spanCloseModalBio = document.getElementById('close-bio');

// Open the bio modal when the user activates the question-mark button (click or Enter/space key)
function displayModalBio() {
    modalBio.classList.remove('hide');
    modalBio.classList.add('show');
    modalBio.focus();
}

bioTrigger.addEventListener('click', displayModalBio);
bioTrigger.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' || e.key === ' ') {
        displayModalBio();
    }
});

// Close the bio modal when the user activates the x span (click or Enter/space key)
function closeModalBio() {
    modalBio.classList.remove('show');
    modalBio.classList.add('hide');
}

spanCloseModalBio.addEventListener('click', closeModalBio);
spanCloseModalBio.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' || e.key === ' ') {
        closeModalBio();
    }
});

// Close the bio modal when the user clicks anywhere outside of it
window.addEventListener('click', function (e) {
    if (e.target === modalBio) {
        modalBio.classList.add('hide');
    }
});