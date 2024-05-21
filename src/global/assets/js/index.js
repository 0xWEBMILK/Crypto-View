document.addEventListener('DOMContentLoaded', () => {
    const cryptoSelect = document.getElementById('crypto-select');
    const currencySelect = document.getElementById('currency-select');
    const cryptoPrice = document.getElementById('crypto-price');

    cryptoSelect.addEventListener('change', updatePrice);
    currencySelect.addEventListener('change', updatePrice);

    async function updatePrice() {
        const selectedCrypto = cryptoSelect.value;
        const selectedCurrency = currencySelect.value;
        const price = await getCryptoPrice(selectedCrypto, selectedCurrency);

        const currencySymbols = {
            "usd": "$",
            "gbp": "£",
            "rub": "₽"
        };

        cryptoPrice.textContent = `The current price of ${selectedCrypto.charAt(0).toUpperCase() + selectedCrypto.slice(1)} is ${currencySymbols[selectedCurrency]}${price}`;
    }

    async function getCryptoPrice(cryptoId, currency) {
        try {
            const response = await fetch(`https://api.coingecko.com/api/v3/simple/price?ids=${cryptoId}&vs_currencies=${currency}`);
            const data = await response.json();
            return data[cryptoId][currency];
        } catch (error) {
            console.error('Error fetching the crypto price:', error);
            return 'Error fetching price';
        }
    }
});
