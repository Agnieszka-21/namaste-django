console.log("Checking JavaScript for the waiver modal");

/**
 * Control the waiver modal - loosely based on the article from w3schools: https://www.w3schools.com/howto/howto_css_modals.asp
 */
const modalWaiver = document.getElementById('modal-waiver');
const waiverTrigger = document.getElementById('waiver');
const spanCloseModalWaiver = document.getElementById('close-waiver');


// Open the waiver modal when the user activates the question-mark button (click or Enter/space key)
function displayModalWaiver() {
    modalWaiver.classList.remove('hide');
    modalWaiver.classList.add('show');
    modalWaiver.focus();
    trapFocus();
}

waiverTrigger.addEventListener('click', displayModalWaiver);
waiverTrigger.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' || e.key === ' ') {
        displayModalWaiver();
    }
});

// Close the waiver modal when the user activates the x span (click or Enter/space key)
function closeModalWaiver() {
    modalWaiver.classList.remove('show');
    modalWaiver.classList.add('hide');
}

spanCloseModalWaiver.addEventListener('click', closeModalWaiver);
spanCloseModalWaiver.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' || e.key === ' ') {
        closeModalWaiver();
    }
});

// Close the waiver modal when the user clicks anywhere outside of it
window.addEventListener('click', function (e) {
    if (e.target === modalWaiver) {
        modalWaiver.classList.add('hide');
    }
});

// Trap focus in the bio modal - adapted from the following article: 
// https://hidde.blog/using-javascript-to-trap-focus-in-an-element/

function trapFocus() {
    const focusableElWaiver = modalWaiver.querySelector('#close-waiver');
    const KEYCODE_TAB = 9;

    modalWaiver.addEventListener('keydown', function (e) {
        let isTabPressed = (e.key === 'Tab' || e.keyCode === KEYCODE_TAB);

        if (!isTabPressed) {
            return;
        }

        if (e.shiftKey) /* shift + tab */ {
            if (document.activeElement === modalWaiver) {
                e.preventDefault();
            }
        } else /* tab */ {
            if (document.activeElement === focusableElWaiver) {
                e.preventDefault();
            }
        }
    });
}


// Following code losely based on this article: 
// https://www.geeksforgeeks.org/how-to-get-selected-value-in-dropdown-list-using-javascript/ 
const bookingBtn = document.querySelector('#booking-submit');
bookingBtn.addEventListener('click', getOption);
bookingBtn.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' || e.key === ' ') {
        getOption();
    }
});

function getOption() {
    const selectElement = document.querySelector('#available-dates');
    let chosenOption = selectElement.value;
    console.log(chosenOption);
}

// Further steps to convert that into python: 
// https://www.makeuseof.com/run-javascript-in-python/#:~:text=The%20first%20step%20is%20the,console%20windows%20of%20the%20browser.
