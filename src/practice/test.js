function datescounting(a, b) {
    var result = 0;
    for (var i = 0; i < a.length; i++) {
        if (a[i] < b[i]) {
            result++;
        }
    }
    return result;
}


