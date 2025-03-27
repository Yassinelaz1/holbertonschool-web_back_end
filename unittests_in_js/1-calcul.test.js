const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', function () {
    it('should return the sum of rounded numbers', function () {
        assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
        assert.strictEqual(calculateNumber('SUM', 1.2, 3.7), 5);
        assert.strictEqual(calculateNumber('SUM', 1.5, 3.7), 6);
    });

    it('should return the subtraction of rounded numbers', function () {
        assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
        assert.strictEqual(calculateNumber('SUBTRACT', 2.6, 1.2), 2);
        assert.strictEqual(calculateNumber('SUBTRACT', 3.9, 0.2), 4);
    });

    it('should return the division of rounded numbers', function () {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
        assert.strictEqual(calculateNumber('DIVIDE', 9.6, 2.1), 5);
    });

    it('should return "Error" when dividing by 0', function () {
        assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
        assert.strictEqual(calculateNumber('DIVIDE', 5.8, 0.4), 'Error');
    });

    it('should throw an error for invalid operation types', function () {
        assert.throws(() => calculateNumber('MULTIPLY', 1, 2), Error, 'Invalid operation type');
    });
});
