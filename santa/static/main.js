function allLetter(inputtxt) {
    let letters = /^[0-9a-zA-ZА-ЯЁа-яё,\.!:?\-]+$/;
    if (!inputtxt.value.match(letters)) {
        alert('Можно использовать только текст');
    }
}