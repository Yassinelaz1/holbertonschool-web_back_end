const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', function () {
    let stub, consoleSpy;

    beforeEach(() => {
        // Stub Utils.calculateNumber to always return 10
        stub = sinon.stub(Utils, 'calculateNumber').returns(10);
        // Spy on console.log to check the output
        consoleSpy = sinon.spy(console, 'log');
    });

    afterEach(() => {
        // Restore the original function and console.log
        stub.restore();
        consoleSpy.restore();
    });

    it('should stub Utils.calculateNumber and log correct message', function () {
        sendPaymentRequestToApi(100, 20);

        // Check if the stub was called correctly
        expect(stub.calledOnce).to.be.true;
        expect(stub.calledWith('SUM', 100, 20)).to.be.true;

        // Check if console.log printed the correct message
        expect(consoleSpy.calledOnceWithExactly('The total is: 10')).to.be.true;
    });
});
