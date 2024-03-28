// 문자열 안에 문자열
// str1 안에 str2가 있다면 1 아님 2 리턴
// includes 함수가 존재한다.
function solution(str1, str2) {
    if(str1.includes(str2)){
        return 1
    }else{
        return 2
    }
}

console.log(solution("ab6CDE443fgh22iJKlmn1o","6CD"));