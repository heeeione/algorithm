function solution(d, budget) {
    let answer = 0;
    let total = 0;
    d.sort((a,b) => a-b);
    for (let i=0; i<d.length; i++) {
        total += d[i];
        if (total > budget) break
        answer++;
    }
    return answer;
}