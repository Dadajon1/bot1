import paypalrestsdk
paypalrestsdk.configure({
  "mode": "sandbox", # sandbox or live
  "client_id": "EBWKjlELKMYqRNQ6sYvFo64FtaRLRR5BdHEESmha49TM",
  "client_secret": "EO422dn3gQLgDbuwqTjzrFgFtaRLRR5BdHEESmha49TM" })

payment = paypalrestsdk.Payment({
    "intent": "sale",
    "payer": {
        "payment_method": "paypal"},
    "redirect_urls": {
        "return_url": "http://localhost:3000/payment/execute",
        "cancel_url": "http://localhost:3000/"},
    "transactions": [{
        "item_list": {
            "items": [{
                "name": "item",
                "sku": "item",
                "price": "5.00",
                "currency": "USD",
                "quantity": 1}]},
        "amount": {
            "total": "5.00",
            "currency": "USD"},
        "description": "This is the payment transaction description."}]})


if payment.create():
  print("Payment created successfully")
else:
  print(payment.error)

print(payment)
for link in payment.links:
    # print(link)
    if link.rel == "approval_url":
        approval_url = str(link.href)
        # print("Redirect for approval: %s" % (id))
# #
# # Fetch Payment
payment = paypalrestsdk.Payment.find("PAYID-MGXF2EA3X661791YH733221V")
#
print(payment)
# Get List of Payments
payment_history = paypalrestsdk.Payment.all({"count": 10})
print(payment_history)

