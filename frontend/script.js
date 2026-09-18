const sendButton = document.getElementById("send-button");

sendButton.addEventListener("click", () => {
    const name = document.getElementById("name").value;
    const message = document.getElementById("message").value;

    fetch("http://127.0.0.1:8000/chat/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: name,
            message: message
        })
    });
});