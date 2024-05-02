// 모음제거
// a,e,i,o,u = 모음 문자열에 포함이면 제거

function solution(my_string) {
    return my_string.replace(/a|e|i|o|u/gi,'');
}

console.log(solution("bus")); // "bs"