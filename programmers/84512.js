const arr = ['A', 'E', 'I', 'O', 'U']
var cnt = 0
var answer = 21e5
function dfs(level, now, target) {
    if (now === target) {
        if (answer > cnt) {
            answer = cnt
        }
        return
    }
    cnt ++

    if (level === 5) {
        return
    }

    for (var i=0; i<5; i++) {
        now += arr[i]
        dfs(level+1, now, target)
        now = now.slice(0,level)
    }
}


function solution(word) {
    dfs(0,'', word)
    return answer;
}
