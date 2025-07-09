# 6. Pricing

##  Subscription, Payment and Cancellation

7 days free trial, then you will be charged monthly at one of the following rates (excluding tax) for the Pro Features. You can cancel your subscription at any time before the 7th day, and you will not be charged:
- USD US$2.66 / month, excluding tax, tax will be automatically calculated based on your location.
- Price in EUR, CNY, HKD will be automatically calculated and displayed based on your location.

Each Pro Code can offer 10 devices to access Pro Features.After the 7 day trial period, you may cancel your subscription at any time, which will take effect at the end of your current billing cycle.

Each Pro code is valid for both Excel-to-JSON and [JSON-to-Excel](https://json-to-excel.wtsolutions.cn/en/latest/) add-in provided by WTSolutions.

### Subscribe though Paddle

#### Payment Methods
- Paypal
- Credit Card/Debit Card with Visa, Mastercard, American Express, Maestro, Cartes Bancaires, Dankort, UnionPay, Mada, JCB, Diners Club, and Discover.
- Google Pay (Chrome or Android device required)
- Apple Pay (Apple Device required)
- BanContact in BE

<script src="https://cdn.paddle.com/paddle/v2/paddle.js"></script>
<script type="text/javascript">
  // Paddle.Environment.set("sandbox");
  Paddle.Initialize({ 
    token: "live_1c12997e01d459f8b047201cd55"
  });
  function checkoutnow(){
    Paddle.Checkout.open({
        items: [{priceId: 'pri_01jz0fdq3rm19fn5bqrn86tnjy',quantity: 1}]
    });  
  }  
</script>

### Subscribe Now

<button onclick='checkoutnow()'>Start 7 Day Free Trial Now</button>

For subscription terms, kindly refer to the [Terms of Use](termsofuse.md)

### Cancel or Manage Subcription (Paddle)

You can cancel your subscription at any time. After the current billing cycle ends, you will no longer have access to the pro features. Management of subscription can be performed through paddle customer portal.

[https://customer-portal.paddle.com/cpl_01jxkve1dh6g9v8j172pybc4nf](https://customer-portal.paddle.com/cpl_01jxkve1dh6g9v8j172pybc4nf)

### Cancel or Manage Subcription (Stripe)

You can cancel your subscription at any time. After the current billing cycle ends, you will no longer have access to the pro features.

[https://billing.stripe.com/p/login/5kQ4gyadZ7p22JY3V83Je00](https://billing.stripe.com/p/login/5kQ4gyadZ7p22JY3V83Je00)