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

    let getLongestCommonPrefix = function(strings) {
        let _cmp = function(a, b) {
            if (a.length < b.length) {
                return -1;
            } else if (a.length > b.length) {
                return 1;
            } else { return 0; }
        };
        const sortedStrings = strings.slice();
        sortedStrings.sort(_cmp);

        let lcp = '';
        let shortest = sortedStrings.shift();
        for (let i = 0; i < shortest.length; i++) {
            for (let j = 0; j < sortedStrings.length; j++) {
                if (sortedStrings[j][i] !== shortest[i]) {
                    return lcp;
                }
            }
            lcp += shortest[i];
        }
        return lcp;
    };

    var isAdditiveNumber = function(s) {
        if (s.length < 3) { return false; }

        // leading zeros not allowed
        if (s[0] === '0') { return false; }

        // select initial two numbers
        for (var len1 = 1; len1 <= s.length - 2; len1++) {
            var a = parseInt(s.substr(0, len1));
            var remaining = s.substr(len1);
            for (var len2 = 1; len2 <= remaining.length - 1; len2++) {
                // leading zeros not allowed, but 0 itself is allowed
                if (remaining[0] !== '0' || len2 === 1) {
                    var b = parseInt(remaining.substr(0, len2));
                    var progress = [a, b];
                    var newRemaining = remaining.substr(len2);
                    if (_isAdditiveNumber(progress, newRemaining)) {
                        return true;
                    }
                }
            }
        }

        return false;
    };

    var _isAdditiveNumber = function(progress, remaining) {
        if (remaining.length === 0 && progress.length > 2) {
            return true;
        }

        if (remaining[0] === '0') {
            return false;
        }

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
    };

    let isOneAway = function(s1, s2) {
        if (s1.length === s2.length) {
            return _isOneAwayReplaced(s1, s2);
        } else if (s1.length - s2.length === 1) {
            return _isOneAwayInserted(s1, s2);
        } else if (s2.length - s1.length === 1) {
            return _isOneAwayInserted(s2, s1);
        }
        return false;
    };

    let _isOneAwayReplaced = function(s1, s2) {
        let foundDiff = false;
        for (let i = 0; i < s1.length; i++) {
            if (s1[i] !== s2[i]) {
                if (foundDiff) {
                    return false;
                }
                foundDiff = true;
            }
        }
        return foundDiff;
    };

    /**
     * where s1 = s2.insert(i, c)
     */
    let _isOneAwayInserted = function(s1, s2) {
        let offset = 0;
        let i = 0;
        while (i < s2.length) {
            if (s1[i + offset] !== s2[i]) {
                if (offset > 0) {
                    return false;
                }
                offset++;
            } else {
                i++;
            }
        }
        return true;
    };

    return {
        'isAdditiveNumber': isAdditiveNumber,
        'getLongestCommonPrefix': getLongestCommonPrefix,
        'isOneAway': isOneAway
    };

})();


exports.Sort = Sort;
exports.Misc = Misc;
