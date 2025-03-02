function translateText() {
    // Get the value entered by the user in the input field
    let inputText = document.getElementById('inputText').value;

    // This is where you would typically connect to a translation API
    // For now, let's mock a simple translation for demonstration
    let translation = "";

    // Example logic for mocking translation
    if (inputText.toLowerCase() === "break a leg") {
        translation = "Good luck (usually used before a performance).";
    } else {
        translation = "Translation not found.";
    }

    // Display the translation in the result section
    document.getElementById('outputText').innerText = translation;
}