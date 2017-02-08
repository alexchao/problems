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
        if (j - i == 0) { return; }
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


exports.Sort = Sort;
