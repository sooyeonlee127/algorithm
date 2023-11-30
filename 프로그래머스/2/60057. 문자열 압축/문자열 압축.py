def solution(s):
    answer = len(s)
    for n in range(2, len(s)//2+1):
        result = ''
        temp = s[:n]
        cnt = 1
        for i in range(n, len(s), n):
            if temp == s[i:i+n]:
                cnt+=1
            else:
                if cnt != 1:
                    result += str(cnt)
                result += temp
                temp = s[i:i+n]
                cnt = 1
        if cnt != 1:
            result += str(cnt)
        result +=temp
        answer = min(len(result), answer)
        
    return answer