document.addEventListener("DOMContentLoaded", () => {
    const conversionForm = document.getElementById("conversionForm");
    const resultDisplay = document.getElementById("conversionResult");

    conversionForm.addEventListener("submit", async (event) => {
        event.preventDefault();

        const crypto = document.getElementById("crypto").value.trim().toLowerCase();
        const currency = document.getElementById("currency").value.trim().toLowerCase();

        try {
            // Fetch the conversion rate from the CoinGecko API
            const response = await fetch(`https://api.coingecko.com/api/v3/simple/price?ids=${crypto}&vs_currencies=${currency}`);
            const data = await response.json();

            console.log(data); // Debug: Check the full API response

            // Check if the response contains the expected data
            if (data[crypto] && data[crypto][currency]) {
                const rate = data[crypto][currency];

                resultDisplay.innerHTML = `
                    <p>1 <strong>${crypto}</strong> = <strong>${rate}</strong> <strong>${currency.toUpperCase()}</strong></p>
                `;
                resultDisplay.classList.remove("hidden");
                resultDisplay.classList.remove("text-red-500");
                resultDisplay.classList.add("text-yellow-700", "bg-yellow-100", "border-yellow-500");
            } else {
                throw new Error("Invalid cryptocurrency or currency.");
            }
        } catch (err) {
            resultDisplay.textContent = "Something went wrong, please check you internet connection and try again after some time.";
            resultDisplay.classList.remove("hidden");
            resultDisplay.classList.add("text-red-600", "bg-red-100", "border-red-500");
        }
    });
});
