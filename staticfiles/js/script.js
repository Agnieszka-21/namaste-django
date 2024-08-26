console.log("Checking JavaScript");

/**
 * Control the waiver modal - loosely based on the article from w3schools: https://www.w3schools.com/howto/howto_css_modals.asp
 */
const modalWaiver = document.getElementById('modal-waiver');
const waiverTrigger = document.getElementById('waiver');
const spanCloseModalWaiver = document.getElementById('close-waiver');

// Control the teacher bio modal
const modalBio = document.getElementById('modal-bio');
const bioTrigger = document.getElementById('teacher-bio');
const spanCloseModalBio = document.getElementById('close-bio');


// Open the waiver modal when the user activates the question-mark button (click or Enter/space key)
function displayModalWaiver() {
    modalWaiver.classList.remove('hide');
    modalWaiver.classList.add('show');
    modalWaiver.focus();
}

waiverTrigger.addEventListener('click', displayModalWaiver);
waiverTrigger.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' || e.key === ' ') {
        displayModalWaiver();
    }
});

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

// Close the waiver modal when the user activates the x span (click or Enter/space key)
function closeModalWaiver() {
    modalBio.classList.remove('show');
    modalWaiver.classList.add('hide');
}

spanCloseModalWaiver.addEventListener('click', closeModalWaiver);
spanCloseModalWaiver.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' || e.key === ' ') {
        closeModalWaiver();
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

// Close the waiver modal when the user clicks anywhere outside of it
window.addEventListener('click', function (e) {
    if (e.target === modalWaiver) {
        modalWaiver.classList.add('hide');
    }
});

// Close the bio modal when the user clicks anywhere outside of it
window.addEventListener('click', function (e) {
    if (e.target === modalBio) {
        modalBio.classList.add('hide');
    }
});