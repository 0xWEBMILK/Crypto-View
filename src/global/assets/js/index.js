const input = document.getElementById('coininput')
const text = document.getElementById('coinsure')


input.addEventListener('input', () => {
    if (input.value.length !== 0) {
        text.innerHTML = `Do you really want to get the <b>${input.value}</b> currency rate?`
    } else {
        text.innerHTML = `Welcome to Crypto App!`
    }
})