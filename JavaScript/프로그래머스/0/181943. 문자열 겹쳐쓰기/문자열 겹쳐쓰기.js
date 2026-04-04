function solution(my_string, overwrite_string, s) {
    let answer = [...my_string];
    answer.splice(s, overwrite_string.length, overwrite_string);
    // splice(startIndex, deleteLength, changeItem) 순으로 작성
    // startIndex에서 deleteLength만큼을 changeItem으로 대체한다 
    return answer.join('');
}