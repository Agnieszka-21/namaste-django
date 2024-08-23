console.log("Checking JavaScript");

/**
 * Control the ASMR Modal - loosely based on the article from w3schools: https://www.w3schools.com/howto/howto_css_modals.asp
 */
const modalWaiver = document.getElementById('modal-waiver');
const thisWaiver = document.getElementById('waiver');
const spanCloseModalWaiver = document.getElementById('close-waiver');


// Open the ASMR modal when the user activates the question-mark button (click or Enter/space key)
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

// Close the modal when the user activates the x span (click or Enter/space key)
spanCloseModalWaiver.addEventListener('click', closeModalWaiver);
spanCloseModalWaiver.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' || e.key === ' ') {
        closeModalWaiver();
    }
});

function closeModalWaiver() {
    modalWaiver.classList.add('hide');
}

// Close the modal when the user activates the okay button (click or Enter/space key)
modalAsmrBtn.addEventListener('click', closeModalWaiver);
modalAsmrBtn.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' || e.key === ' ') {
        closeModalWaiver();
    }
});

// Close the modal when the user clicks anywhere outside of it
window.addEventListener('click', function (e) {
    if (e.target === modalWaiver) {
        modalWaiver.classList.add('hide');
    }
});