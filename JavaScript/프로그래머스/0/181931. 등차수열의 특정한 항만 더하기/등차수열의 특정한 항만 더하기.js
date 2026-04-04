// 등차수열: 각 항이 일정한 수를 더하여 만들어지는 수열
// 공차: 수열에서 연속하는 두 항 사이의 일정한 차이

function solution(a, d, included) {
  let res = 0;
  for (let i = 0; i < included.length; i++) {
    if (included[i]) res += a + d * i;
  }
  return res;
}