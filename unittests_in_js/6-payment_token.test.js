const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', function () {
    it('should return a resolved promise with correct data when success is true', function (done) {
        getPaymentTokenFromAPI(true)
            .then(response => {
                expect(response).to.be.an('object');
                expect(response).to.have.property('data', 'Successful response from the API');
                done(); // Call done() to indicate test completion
            })
            .catch(err => done(err)); // In case of an error, fail the test
    });
});
