function solution(str1, str2) {
    const res = [...str1].map((currentValue, index) => currentValue+str2[index]);
    // srt1의 currentValue와 str2[index]를 이은 값을 리턴한다
    return res.join("");
}