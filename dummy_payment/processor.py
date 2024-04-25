import uuid
import random

def process_payment(amount, payment_method):
    transaction_id = str(uuid.uuid4())
    is_successful = random.choice([True, False])

    return {
        'transaction_id': transaction_id,
        'amount': amount,
        'is_successful': is_successful,
        'payment_method': payment_method
    }
