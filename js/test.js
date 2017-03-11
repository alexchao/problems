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

    var assertStrictEqual = function(a, b) {
        if (a === b) { return; }
        throw new Error(`${a.toString()} !== ${b.toString()}`);
    };


    var assertEqual = (a, b) => { assertStrictEqual(a, b); };

    var assertNull = function(x) {
        assertStrictEqual(x, null);
    };

    var assertTrue = function(x) {
        if (x === true) { return; }
        throw new Error('Expected true');
    };

    var assertFalse = function(x) {
        if (x === false) { return; }
        throw new Error('Expected false');
    };

    return {
        'arrayEqual': arrayEqual,
        'assertEqual': assertEqual,
        'assertNull': assertNull,
        'assertTrue': assertTrue,
        'assertFalse': assertFalse,
        'assertStrictEqual': assertStrictEqual
    };

})();


var runTests = function(tests) {
    Object.keys(tests).forEach(function(testName) {
        try {
            tests[testName]();
            console.log(`Test OK "${testName}"`);
        } catch (e) {
            let msg = `Test FAIL "${testName}": "${e.message}"\n`;
            msg += e.stack;
            console.log(msg);
        }
    });
};



exports.Assert = Assert;
exports.runTests = runTests;
