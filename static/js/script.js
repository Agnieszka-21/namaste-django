console.log("Checking JavaScript");

/**
 * Control the waiver modal - loosely based on the article from w3schools: https://www.w3schools.com/howto/howto_css_modals.asp
 */
const modalWaiver = document.getElementById('modal-waiver');
const thisWaiver = document.getElementById('waiver');
const spanCloseModalWaiver = document.getElementById('close-waiver');

// Control the teacher bio modal
const modalBio = document.getElementById('modal-bio');
const teacherBio = document.getElementById('teacher-bio');
const spanCloseModalBio = document.getElementById('close-bio');


// Open the waiver modal when the user activates the question-mark button (click or Enter/space key)
thisWaiver.addEventListener('click', displayModalWaiver);
thisWaiver.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' || e.key === ' ') {
        displayModalWaiver();
    }
});

function displayModalWaiver() {
    modalWaiver.classList.remove('hide');
    modalWaiver.classList.add('show');
    modalWaiver.focus();
}

// Open the bio modal when the user activates the question-mark button (click or Enter/space key)
teacherBio.addEventListener('click', displayModalBio);
teacherBio.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' || e.key === ' ') {
        displayModalBio();
    }
});

function displayModalBio() {
    modalBio.classList.remove('hide');
    modalBio.classList.add('show');
    modalBio.focus();
}

// Close the waiver modal when the user activates the x span (click or Enter/space key)
spanCloseModalWaiver.addEventListener('click', closeModalWaiver);
spanCloseModalWaiver.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' || e.key === ' ') {
        closeModalWaiver();
    }
});

function closeModalWaiver() {
    modalWaiver.classList.add('hide');
}

// Close the bio modal when the user activates the x span (click or Enter/space key)
spanCloseModalBio.addEventListener('click', closeModalBio);
spanCloseModalBio.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' || e.key === ' ') {
        closeModalBio();
    }
});

function closeModalBio() {
    modalBio.classList.add('hide');
}

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