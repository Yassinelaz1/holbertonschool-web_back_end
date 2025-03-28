const sinon = require('sinon');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', function () {
    let consoleSpy;

    beforeEach(() => {
        // Create a spy on console.log before each test
        consoleSpy = sinon.spy(console, 'log');
    });

    afterEach(() => {
        // Restore console.log after each test
        consoleSpy.restore();
    });

    it('should log the correct total for (100, 20)', function () {
        sendPaymentRequestToApi(100, 20);

        // Check if console.log was called once with the correct message
        expect(consoleSpy.calledOnceWithExactly('The total is: 120')).to.be.true;
    });

    it('should log the correct total for (10, 10)', function () {
        sendPaymentRequestToApi(10, 10);

        // Check if console.log was called once with the correct message
        expect(consoleSpy.calledOnceWithExactly('The total is: 20')).to.be.true;
    });
});
