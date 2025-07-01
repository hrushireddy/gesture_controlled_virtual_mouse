// User clicked button
document.getElementById("userInputButton").addEventListener("click", getUserInput, false);

// User pressed enter '13'
document.getElementById("userInput").addEventListener("keyup", function (event) {
    if (event.key === "Enter") {
        // Cancel the default action
        event.preventDefault();
        // Process event
        getUserInput();
    }
});

// Expose functions to Python
eel.expose(addUserMsg);
eel.expose(addAppMsg);

function addUserMsg(msg) {
    console.log("addUserMsg ", msg);
    // const element = document.getElementById("messages");
    // element.innerHTML += '<div class="message from ready rtol">' + msg + '</div>';
    // element.scrollTop = element.scrollHeight - element.clientHeight - 15;
    // // Add delay for animation to complete and then modify class to => "message from"
    // const index = element.childElementCount - 1;
    // setTimeout(changeClass.bind(null, element, index, "message from"), 500);
}

function addAppMsg(msg) {
    console.log("addAppMsg", msg);
    const element = document.getElementById("messages");
    element.innerHTML += '<div class="message to ready ltor" style="text-align: center;">' + msg + '</div>';
    element.scrollTop = element.scrollHeight - element.clientHeight - 15;
    // Add delay for animation to complete and then modify class to => "message to"
    const index = element.childElementCount - 1;
    console.log("asdasd", msg);
    setTimeout(changeClass.bind(null, element, index, "message to"), 500);
}

function changeClass(element, index, newClass) {
    console.log(newClass + ' ' + index);
    element.children[index].className = newClass;
}

function getUserInput() {
    const element = document.getElementById("userInput");
    const msg = element.value;
    if (msg.trim().length !== 0) {
        element.value = "";
        eel.getUserInput(msg);  // Ensure proper Eel call
    }
}