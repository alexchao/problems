var Closure = (function() {
    var getNumberLoggersBad = function(n) {
        var fns = [];
        for (var i = 0; i < n; i++) {
            fns.push(function() {
                console.log(i);
            });
        }
        return fns;
    };

    var getNumberLoggers = function(n) {
        var fns = [];
        for (var i = 0; i < n; i++) {
            fns.push((function(x) {
                return function() { console.log(x); };
            })(i));
        }
        return fns;
    };
    return {
        'getNumberLoggersBad': getNumberLoggersBad,
        'getNumberLoggers': getNumberLoggers
    };
})()

var badLoggers = Closure.getNumberLoggersBad(10);
for (var i = 0; i < badLoggers.length; i++) {
    badLoggers[i]();
}
var loggers = Closure.getNumberLoggers(10);
for (var i = 0; i < loggers.length; i++) {
    loggers[i]();
}
