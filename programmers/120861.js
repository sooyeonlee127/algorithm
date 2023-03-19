function solution(keyinput, board) {
    var answer = [];
    var direct = {'up': [1,0], 'down': [-1,0], 'left':[0,-1], 'right':[0,1]}
    var y = 0;
    var x = 0;
    var standx = parseInt(board[0]/2)
    var standy = parseInt(board[1]/2)
    for (var i=0; i < keyinput.length; i++) {
        var dy = y + direct[keyinput[i]][0];
        var dx = x + direct[keyinput[i]][1];
        if ( dy >= standy*(-1) && dy <= standy && dx >= standx*(-1) && dx <= standx) {
            y = y + direct[keyinput[i]][0]
            x = x + direct[keyinput[i]][1]
        }
    }
    answer = [x,y]
   
    return answer;
}
