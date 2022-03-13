

function mobileNav() {
    var x = document.getElementById("mobileNav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}

function addCalendar() {
    var calendar = document.getElementById("calendar");
    
    const date = new Date();

    const year = date.getFullYear();    
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');

    const today = [year, month, day].join('-');

    calendar.innerHTML += `<input type="date" name="date" value="${today}" min="${today}">`;
}

function fillDropdown() {
    var guestDropdown = document.getElementById("guestDropdown");
    
    for (let i = 0; i < 25; i++) {
        guestDropdown.innerHTML += `<option value="${i}">${i}</option>`;
    }


}

window.onload = function() {
    fillDropdown();
    addCalendar();
}