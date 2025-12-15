// javascript will be written here
// make the confetti


const button = document.querySelector('#event_button');
console.log(button)
const form = document.querySelector('#form')
const jsConfetti = new JSConfetti();
const updateTarget = document.getElementById('status');
let slideIndex = 0;
showSlides();

console.log(button)
console.log(form)

document.addEventListener('DOMContentLoaded', function () {
    const button = document.querySelector('#event_button');
    const form = document.querySelector('#form');

    console.log(button);
    console.log(form);

    if (form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            setTimeout(() => {
                this.submit();
                console.log('Form submitted after delay');
            }, 800);
        });
    }

    if (button) {
        button.addEventListener('click', () => {
            jsConfetti.addConfetti();
        });
    }
});

// form.addEventListener('submit', function(event) {
//     event.preventDefault();
//     // Delay submission by 5 seconds (5000 milliseconds)
//     setTimeout(() => {
//         this.submit(); // Submit the form after the delay
//         console.log('Form submitted after delay');
//     }, 800);
// });

// button.addEventListener('click', () => {
//     jsConfetti.addConfetti();
// })


function showSlides() {
    let slides = document.getElementsByClassName("mySlides");
    if (!slides || slides.length === 0) {
        return;
    }
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) {
        slideIndex = 1;
    }
    slides[slideIndex - 1].style.display = "block";
    setTimeout(showSlides, 3500);
}