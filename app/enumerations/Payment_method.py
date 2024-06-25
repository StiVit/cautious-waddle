from enum import StrEnum

class PaymentMethod(StrEnum):
    CREDIT_CARD = "Credit Card"
    PAYPAL = "PayPal"
    DEBIT_CARD = "Debit Card"