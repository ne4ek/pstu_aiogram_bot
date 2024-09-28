function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
const progress = document.querySelector(".progress");

async function load() {
  for (let i = 0; i <= 100; i++) {
    if (i < 70) await sleep(10);
    else await sleep(20);
    progress.style.width = i + "%";
  }
}

load();
