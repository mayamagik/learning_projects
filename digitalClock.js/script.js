
//DIGITAL CLOCK

function updateCLock() {

    const now = new Date();
    let hours = now.getHours().toString().padStart(2, 0);
    //const meridiem = hours >= 12 ? "PM" : "AM";
    // hours = hours % 12 || 12;
    // hours = hours.toString().padStart(2,0);
    const minutes = now.getMinutes().toString().padStart(2, 0);
    const seconds = now.getSeconds().toString().padStart(2, 0);
    const timeString = `${hours}:${minutes}:${seconds}` //${meridiem};
    document.getElementById("clock").textContent = timeString;

}
updateCLock(); // update clock immediately after opening the program
setInterval(updateCLock, 1000);

