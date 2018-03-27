# Good friends

You are going on a road trip with your friends.
There are 4 of you in a rental car : Alice, Bob, Claire and David.
You are touring Ireland mainly because you all like stout.

You don't really know how long you will stay there, nor the price of gas or affordable BnB availabilities... so you just can't draft a budget for this trip.

You decided with your friends that it would be easier if each one would pay some stuff everyday, then sort out who owes money to who once you are back home.

## Features

Examples are given in pseudo-code.

### Registering a payment

+ Alice paid an irish coffee for herself, Bob and Claire (but not David). The bill amount was 15 €.

```python
payment_history.register_payment(15, 'Alice', ['Alice', 'Bob', 'Claire'])
```

+ David paid a pint of guinness for Alice and Claire (but not to himself and not to Bob). The bill amount was 8 €.

```python
payment_history.register_payment(8, 'David', ['Alice', 'Claire'])
```

+ Bob paid lunch for everyone (pub's food is the best here). The bill amount was 32 €.

```python
payment_history.register_payment(32, 'Bob', ['Alice', 'Bob', 'Claire', 'David'])
```

### Balancing debts

Rather than a very detailed list of debts, the simplified balance is computed by the software and printed out.

```python
>>> payment_history.balance_debts()
>>>
  Alice owes 2 € to Bob
  Bob has no debts.
  Claire owes 17 € to Bob
  David has no debts.
```

### Design constraints

`payment_history` may be a module, class or namespace.
`register_payment` and `balance_debts` are just examples of functions / methods you could use as an entry point for your software.
You are free to stick to them or use different entry points.

### References

This kata is a challenge brought by Abel André (<https://twitter.com/_blndr>).
