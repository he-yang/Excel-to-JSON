# 7. Pricing

<script src="https://cdn.paddle.com/paddle/v2/paddle.js"></script>
<script type="text/javascript">
  // Paddle.Environment.set("sandbox");
  Paddle.Initialize({ 
    token: "live_1c12997e01d459f8b047201cd55"
  });
  function checkoutnow(priceId){
    Paddle.Checkout.open({
        items: [{priceId: priceId,quantity: 1}]
    });  
  }  
</script>

##  Subscription, Payment and Cancellation

7 days free trial, then you will be charged monthly at one of the following rates (excluding tax) for the Pro Features. You can cancel your subscription at any time before the 7th day, and you will not be charged:

| Billing Cycle | Price (USD) | Subscribe through Paddle |
| :---: | :---: | :---: |
| Every Month | US$2.66, excluding tax | <button onclick='checkoutnow("pri_01jz0fdq3rm19fn5bqrn86tnjy")'>Free Trial and Subscribe</button> |
| Every Quarter (3 months) | US$3.66, excluding tax | <button onclick='checkoutnow("pri_01k19xzfq77gp4tvtqypjyfqdq")'>Free Trial and Subscribe</button> |
| Every Half year (6 months) | US$4.99, excluding tax | <button onclick='checkoutnow("pri_01k19y29j38js9zwnq36tkwkqv")'>Free Trial and Subscribe</button> |
| Every Year | US$5.99, excluding tax | <button onclick='checkoutnow("pri_01k19y3basxqvta0cycksqsjaf")'>Free Trial and Subscribe</button> |


* Price in EUR, CNY, HKD will be automatically calculated and displayed based on your location.
* Tax will be automatically calculated based on your location.

Each Pro Code can offer 10 devices to access Pro Features.After the 7 day trial period, you may cancel your subscription at any time, which will take effect at the end of your current billing cycle.

Each Pro code is valid for both Excel-to-JSON and [JSON-to-Excel](https://json-to-excel.wtsolutions.cn/en/latest/) add-in provided by WTSolutions:
- Excel to JSON [Web App](WebApp.md)
- Excel to JSON [Excel Addin](ExcelAddIn.md)
- Excel to JSON [API](API.md)
- JSON to Excel Web App
- JSON to Excel Excel Addin

### Subscribe though Paddle

The subscription is managed through [Paddle](https://paddle.com/). 

#### Payment Methods
- Paypal
- Credit Card/Debit Card with Visa, Mastercard, American Express, Maestro, Cartes Bancaires, Dankort, UnionPay, Mada, JCB, Diners Club, and Discover.
- Google Pay (Chrome or Android device required)
- Apple Pay (Apple Device required)
- BanContact in BE



### Subscribe Now

<button onclick='checkoutnow("pri_01jz0fdq3rm19fn5bqrn86tnjy")'>Start 7 Day Free Trial Now, then USD $2.66 / month (excluding tax)</button>
<button onclick='checkoutnow("pri_01k19xzfq77gp4tvtqypjyfqdq")'>Start 7 Day Free Trial Now, then USD $3.66 / quarter (3 months) (excluding tax)</button>
<button onclick='checkoutnow("pri_01k19y29j38js9zwnq36tkwkqv")'>Start 7 Day Free Trial Now, then USD $4.99 / half year (6 months) (excluding tax)</button>
<button onclick='checkoutnow("pri_01k19y3basxqvta0cycksqsjaf")'>Start 7 Day Free Trial Now, then USD $5.99 / year (excluding tax)</button>

For subscription terms, kindly refer to the [Terms of Use](termsofuse.md)

### Cancel or Manage Subcription (Paddle)

You can cancel your subscription at any time. After the current billing cycle ends, you will no longer have access to the pro features. Management of subscription can be performed through paddle customer portal.

[https://customer-portal.paddle.com/cpl_01jxkve1dh6g9v8j172pybc4nf](https://customer-portal.paddle.com/cpl_01jxkve1dh6g9v8j172pybc4nf)

### Cancel or Manage Subcription (Stripe)

You can cancel your subscription at any time. After the current billing cycle ends, you will no longer have access to the pro features.

[https://billing.stripe.com/p/login/5kQ4gyadZ7p22JY3V83Je00](https://billing.stripe.com/p/login/5kQ4gyadZ7p22JY3V83Je00)


## Aftersale services

You can contact us via email at he.yang@wtsolutions.cn for any questions or concerns. We will try our best to respond you within 24 hours, but not later than 72 hours. Please include your `Pro Code` in the email if your question is related to your subscription.