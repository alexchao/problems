var Assert = (function() {

    var _arrayNotEqualMsg = function(a, b) {
        return 'Arrays not equal: [' + a.toString() + '], ['
                        + b.toString() + ']';
    };

    var arrayEqual = function(a, b) {
        if (a === b) { return; }
        if (a == null || b == null) {
            throw new Error('Found null array');
        }
        if (a.length != b.length) {
            throw new Error(_arrayNotEqualMsg(a, b));
        }

        for (var i = 0; i < a.length; i++) {
            if (a[i] !== b[i]) {
                throw new Error(_arrayNotEqualMsg(a, b));
            }
        }
    };

    return {
        'arrayEqual': arrayEqual
    };

})();


var runTests = function(tests) {
    Object.keys(tests).forEach(function(testName) {
        try {
            tests[testName]();
            console.log(`Test OK "${testName}"`);
        } catch (e) {
            console.log(`Test FAIL "${testName}": "${e.message}"`);
        }
    });
};



exports.Assert = Assert;
exports.runTests = runTests;
