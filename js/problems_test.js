

const Test = require('./test.js');
const A = Test.Assert;
const S = require('./problems.js').Sort;


var mergeSortTests = {
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


Test.runTests(mergeSortTests);
