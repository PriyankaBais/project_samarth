document.addEventListener("DOMContentLoaded", () => {
    const askButton = document.getElementById("ask-button");
    const questionInput = document.getElementById("question-input");
    const answerText = document.getElementById("answer-text");
    const sourcesList = document.getElementById("sources-list");

    askButton.addEventListener("click", async () => {
        const question = questionInput.value;
        if (!question) {
            alert("Please enter a question.");
            return;
        }

        
        answerText.textContent = "Thinking...";
        sourcesList.innerHTML = "";
        askButton.disabled = true;

        try {
        
            const response = await fetch("http://127.0.0.1:5000/ask", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ question: question }),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();

            answerText.textContent = data.answer;

            if (data.sources && data.sources.length > 0) {
                data.sources.forEach(source => {
                    const li = document.createElement("li");
                    li.textContent = source;
                    sourcesList.appendChild(li);
                });
            }

        } catch (error) {
            answerText.textContent = `An error occurred: ${error.message}`;
        } finally {
            askButton.disabled = false; 
        }
    });
});