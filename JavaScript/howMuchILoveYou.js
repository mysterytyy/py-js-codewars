function howMuchILoveYou(nbPetals) {
    let phrases = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    let index = (nbPetals - 1) % phrases.length
    return phrases[index]
}


console.log(howMuchILoveYou(3))