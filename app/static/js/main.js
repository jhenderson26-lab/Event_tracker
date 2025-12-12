// javascript will be written here
// make the confetti


const button = document.querySelector('#event_button');
console.log(button)
const form = document.querySelector('#form')
const jsConfetti = new JSConfetti();
const updateTarget = document.getElementById('status');

console.log(form)

form.addEventListener('submit', function(event) {
        event.preventDefault();

        // Delay submission by 5 seconds (5000 milliseconds)
        setTimeout(() => {
            this.submit(); // Submit the form after the delay
            console.log('Form submitted after delay');
        }, 800);
    });

button.addEventListener('click', () => {
    jsConfetti.addConfetti();
    
})

// button.onclick = function(event) {
//   event.preventDefault();
//   setTimeout(form.submit, 2000);
// }
