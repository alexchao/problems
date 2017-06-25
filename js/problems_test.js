

const Test = require('./test.js');
const Problems = require('./problems.js');
const A = Test.Assert;
const S = Problems.Sort;
const M = Problems.Misc;
const Strings = Problems.Strings;


var TestCases = {};


TestCases.mergeSortTests = {
    'basicSort': function() {
        var d = [5, -1, 200, 43];
        S.mergeSort(d);
        A.arrayEqual(d, [-1, 5, 43, 200]);
    },
    'sortEmpty': function() {
        var d = [];
        S.mergeSort(d);
        A.arrayEqual(d, []);
    },
    'alreadySorted': function() {
        var d = [1, 2, 3];
        S.mergeSort(d);
        A.arrayEqual(d, [1, 2, 3]);
    },
    'oneElement': function() {
        var d = [1];
        S.mergeSort(d);
        A.arrayEqual(d, [1]);
    },
    'twoElements': function() {
        var d = [2,1];
        S.mergeSort(d);
        A.arrayEqual(d, [1,2]);
    }
};


TestCases.isAdditiveNumberTests = {
    'tooShort': function() {
        A.assertFalse(M.isAdditiveNumber('89'));
    },
    'zeros': function() {
        A.assertFalse(M.isAdditiveNumber('000'));
    },
    'zeroOneTwo': function() {
        A.assertFalse(M.isAdditiveNumber('012'));
    },
    'oneTwoThree': function() {
        A.assertTrue(M.isAdditiveNumber('123'));
    },
    'oneTwoThreeFour': function() {
        A.assertFalse(M.isAdditiveNumber('1234'));
    },
    'thousands': function() {
        A.assertTrue(M.isAdditiveNumber('100020003000'));
    },
    'doubleDigits': function() {
        A.assertTrue(M.isAdditiveNumber('199100199'));
    },
    'notAdditiveNumber': function() {
        A.assertFalse(M.isAdditiveNumber('972420823098'));
    },
    'oneOhOne': function() {
        A.assertTrue(M.isAdditiveNumber('101'));
    },
    'base': function() {
        A.assertTrue(M.isAdditiveNumber('112358'));
    }
};


TestCases.getLongestCommonPrefixTests = {
    'base': function() {
        let strings = ['alexchao', 'alex', 'alexander'];
        A.assertStrictEqual(
            M.getLongestCommonPrefix(strings),
            'alex'
            );
    },
    'allEqual': function() {
        let strings = ['brian', 'brian', 'brian'];
        A.assertStrictEqual(
            M.getLongestCommonPrefix(strings),
            'brian'
            );
    },
    'noCommonPrefix': function() {
        let strings = ['alexander', 'brian', 'eric'];
        A.assertStrictEqual(M.getLongestCommonPrefix(strings), '');
    },
    'singleCharPrefix': function() {
        let strings = ['alexander', 'apple', 'artichoke'];
        A.assertStrictEqual(M.getLongestCommonPrefix(strings), 'a');
    }
};


TestCases.isOneAwayTests = {
    'equalStrings': function() {
        A.assertFalse(M.isOneAway('pale', 'pale'));
    },
    'removed': function() {
        A.assertTrue(M.isOneAway('pale', 'ale'));
        A.assertTrue(M.isOneAway('pale', 'ple'));
        A.assertTrue(M.isOneAway('pale', 'pal'));
    },
    'inserted': function() {
        A.assertTrue(M.isOneAway('ale', 'pale'));
        A.assertTrue(M.isOneAway('ple', 'pale'));
        A.assertTrue(M.isOneAway('pal', 'pale'));
    },
    'replaced': function() {
        A.assertTrue(M.isOneAway('pale', 'pace'));
    },
    'replacedTooMany': function() {
        A.assertFalse(M.isOneAway('pale', 'bake'));
    },
    'insertedTooMany': function() {
        A.assertFalse(M.isOneAway('pale', 'apales'));
        A.assertFalse(M.isOneAway('pale', 'paghle'));
    },
};


TestCases.reverseWordsTests = {
    'base': function() {
        A.assertStrictEqual(Strings.reverseWords('dog'), 'dog');
    },
    'twoWords': function() {
        A.assertStrictEqual(Strings.reverseWords('hot dog'), 'dog hot');
    },
    'sentence': function() {
        A.assertStrictEqual(
            Strings.reverseWords("I don't know"),
            "know don't I");
    }
};


Test.runTests(TestCases.mergeSortTests);
Test.runTests(TestCases.isAdditiveNumberTests);
Test.runTests(TestCases.getLongestCommonPrefixTests);
Test.runTests(TestCases.isOneAwayTests);
Test.runTests(TestCases.reverseWordsTests)
