var Sort = (function() {

    var _merge = function(d, i, j, middle) {
        var result = [];
        var x = i, y = middle + 1;
        while (x <= middle && y <= j) {
            if (d[x] < d[y]) {
                result.push(d[x]);
                x++;
            } else {
                result.push(d[y]);
                y++;
            }
        }

        if (x > middle) {
            while (y <= j) {
                result.push(d[y]);
                y++;
            }
        }

        if (y > middle) {
            while (x <= middle) {
                result.push(d[x]);
                x++;
            }
        }

        // copy values
        for (var _i = i, k = 0; _i <= j; _i++, k++) {
            d[_i] = result[k];
        }
    };

    var _mergeSort = function(d, i, j) {
        if (j - i < 1) { return; }
        var middle = Math.floor((j + i) / 2);
        _mergeSort(d, i, middle);
        _mergeSort(d, middle + 1, j);
        _merge(d, i, j, middle);
    };

    var mergeSort = function(d) {
        _mergeSort(d, 0, d.length - 1);
    };

    return {
        'mergeSort': mergeSort
    };
})();


var Misc = (function() {

    var isAdditiveNumber = function(s) {
        return _isAdditiveNumber([], s);
    };

    var _isAdditiveNumber = function(progress, remaining) {
        if (remaining.length === 0 && progress.length > 2) {
            return true;
        }

        if (remaining[0] === '0') {
            return false;
        }

        if (progress.length < 2) {
            var maxLength = remaining.length - (progress.length === 0 ? 2 : 1);
            for (var l = 1; l <= maxLength; l++) {
                var x = remaining.substr(0, l);
                var newProgress = progress.slice();
                newProgress.push(parseInt(x));
                if (_isAdditiveNumber(newProgress, remaining.substr(l))) {
                    return true;
                }
            }
            return false;
        } else {
            var x = progress[progress.length - 2];
            var y = progress[progress.length - 1];
            var sum = x + y;
            var sumAsString = sum + '';
            var sumLength = sumAsString.length;

            if (remaining.length < sumLength) {
                return false;
            }

            if (remaining.substr(0, sumLength) === sumAsString) {
                var newProgress = progress.slice();
                newProgress.push(sum);
                return _isAdditiveNumber(newProgress,
                    remaining.substr(sumLength));
            }
            return false;
        }
    };

    return {
        'isAdditiveNumber': isAdditiveNumber
    };

})();


exports.Sort = Sort;
exports.Misc = Misc;
