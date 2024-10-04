function doubleChar(string){
    let result = ''
    for (let char of string){
        result += char.repeat(2)
    }
    return result
}