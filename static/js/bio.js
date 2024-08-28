console.log("Checking JavaScript - bio modal")

// Control the teacher bio modal
const modalBio = document.getElementById('modal-bio');
const bioTrigger = document.getElementById('bio-modal-trigger');
const spanCloseModalBio = document.getElementById('close-bio');

// Open the bio modal when the user activates the question-mark button (click or Enter/space key)
function displayModalBio() {
    modalBio.classList.remove('hide');
    console.log('Class hide removed');
    modalBio.classList.add('show');
    console.log('Class show added');
    modalBio.focus();
    console.log('Right after modalBio.focus function');
    trapFocus();
    console.log('Right after trapFpcus function');
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


//https://uxdesign.cc/how-to-trap-focus-inside-modal-to-make-it-ada-compliant-6a50f9a70700
//https://vaskort.com/a-trap-focus-function-you-need-for-your-modals/const trapFocus = ((element, prevFocusableElement = document.activeElement) => {

function trapFocus() {
    const focusableElBio = modalBio.querySelector('#close-asmr');
    const KEYCODE_TAB = 9;

    modalBio.addEventListener('keydown', function (e) {
        let isTabPressed = (e.key === 'Tab' || e.keyCode === KEYCODE_TAB);

        if (!isTabPressed) {
            return;
        }

        if (e.shiftKey) /* shift + tab */ {
            if (document.activeElement === modalBio) {
                focusableElBio.focus();
                e.preventDefault();
            }
        } else /* tab */ {
            if (document.activeElement === focusableElBio) {
                modalBio.focus();
                e.preventDefault();
            }
        }
    });
}