const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai.js');

describe('calculateNumber', function () {
    it('should return the sum of rounded numbers', function () {
        expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
        expect(calculateNumber('SUM', 1.2, 3.7)).to.equal(5);
        expect(calculateNumber('SUM', 1.5, 3.7)).to.equal(6);
    });

    it('should return the subtraction of rounded numbers', function () {
        expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
        expect(calculateNumber('SUBTRACT', 2.6, 1.2)).to.equal(2);
        expect(calculateNumber('SUBTRACT', 3.9, 0.2)).to.equal(4);
    });

    it('should return the division of rounded numbers', function () {
        expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
        expect(calculateNumber('DIVIDE', 9.6, 2.1)).to.equal(5);
    });

    it('should return "Error" when dividing by 0', function () {
        expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
        expect(calculateNumber('DIVIDE', 5.8, 0.4)).to.equal('Error');
    });

    it('should throw an error for invalid operation types', function () {
        expect(() => calculateNumber('MULTIPLY', 1, 2)).to.throw(Error, 'Invalid operation type');
    });
});
