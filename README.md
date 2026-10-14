# StreamCommerce

What should happen when the same purchase request arrives twice? This small Python ledger focuses on that question.

Purchases are stored in SQLite with a unique request ID. Repeating a request with the same details leaves the ledger unchanged; reusing its ID with different details raises an error. Revenue is summed in integer cents.

## Try the example

Requires Python 3.10 or newer, with no extra packages.

```sh
git clone https://github.com/priyamukkapati/StreamCommerce.git
cd StreamCommerce
python3 app.py
python3 -m unittest discover -s tests -v
```

The example retries a subscription, adds a gift, and prints `Creator revenue: $6.99`. The retry is counted only once.

The test checks duplicate requests, conflicting amounts, unchanged revenue after a rejected request, and negative-amount validation.

## Storage and scope

The example uses an in-memory database. Passing `Store("purchases.db")` saves the ledger locally. This records purchase data; it does not charge a customer or manage recurring billing. There is no network API or authentication.

The next useful check is concurrent requests from separate database connections, followed by reopening the ledger and verifying the total.
