const BUTTONS_IDS = [
  "napravlenia",
  "stoimost",
  "obshejitie",
  "contacti",
  "anketi",
  "eksameni",
  "postuplenie",
  "ligoti",
  "o_vuse",
];


const BUTTONS_OBJECTS = [];

function fillingButtonsObjects() {
  for (let i = 0; i < BUTTONS_IDS.length; i++) {
    let id = BUTTONS_IDS[i];
    let button = document.getElementById(id);
    BUTTONS_OBJECTS.push(button);
  }
}

function addEventListenerForButtons() {
  for (let i = 0; i < BUTTONS_IDS.length; i++) {
    let button = BUTTONS_OBJECTS[i];
    button.addEventListener("click", () => (goToMenuPage(button.id)));
  }
}

function main() {
  fillingButtonsObjects();
  addEventListenerForButtons();
}

main();
