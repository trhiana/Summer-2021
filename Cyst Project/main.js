

// Get each modal and close button
const buttons = document.getElementsById("myBtn");
const buttonArray = Array.from(buttons).entries();
const modals = document.getElementsByClassName("modal");
const closeButtons = document.getElementsByClassName("close");


for (let [index, button] of buttonArray) {
  const toggleModal => () {
    modals[index].classList.toggle("show-modal");
  };
  button.addEventListener("click", toggleModal);
  closeButtons[index].addEventListener("click", toggleModal);
}

