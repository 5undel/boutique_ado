var stripe_public:key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret:key = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var card = elements.create('card',  {style: style});

var style = {
    color: '#000';
    fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
    fontSmoothing: 'antialiased',
    '::placeholder': {
        color: '#aab7c4'
    }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

card.mount('#card-element');