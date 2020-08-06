invoice_total = 1200
discount = .15
if invoice_total >= 500:
    discount_percent = .2
    print (invoice_total*discount_percent)
elif invoice_total >= 250:
    discount_percent = .1
    print(invoice_total * discount_percent)
elif invoice_total > 0:
    discount_percent = 0
    print(invoice_total * discount_percent)
else:
    print("Invoice total must be greater than zero.")
