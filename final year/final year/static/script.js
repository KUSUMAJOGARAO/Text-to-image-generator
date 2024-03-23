document.getElementById("imageForm").addEventListener("submit", function(event) {
    event.preventDefault();

    var textPrompt = document.getElementById("textPrompt").value;

    fetch('/generate_image', {
        method: 'POST',
        body: new URLSearchParams({
            'textPrompt': textPrompt
        }),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    })
    .then(response => response.json())
    .then(data => {
        var imageResult = document.getElementById("imageResult");
        imageResult.innerHTML = '<img src="' + data.image_path + '" alt="Generated Image">';
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
