function solution(str1, str2) {
    const res = [...str1].map((a, b) => a+str2[b]);
    return res.join("");
}