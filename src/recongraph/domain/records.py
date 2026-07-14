from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass(frozen=True)
class PurchaseRecord:
    """Represent purchase-side financial evidence."""

    record_id: str

    vendor_name: str | None
    reference: str | None
    amount: Decimal
    record_date: date
    tax_identity: str | None
    net_amount: Decimal | None = None
    tax_amount: Decimal | None = None
    tax_rate: Decimal | None = None
    currency: str = "USD"
    sign: int = 1


@dataclass(frozen=True)
class GSTRecord:
    """Represent GST-side financial evidence."""

    record_id: str

    vendor_name: str | None
    reference: str | None
    amount: Decimal
    record_date: date
    tax_identity: str | None
    net_amount: Decimal | None = None
    tax_amount: Decimal | None = None
    tax_rate: Decimal | None = None
    currency: str = "USD"
    sign: int = -1


@dataclass(frozen=True)
class InvoiceRecord:
    """Represent invoice-side financial evidence."""

    record_id: str

    vendor_name: str | None
    reference: str | None
    amount: Decimal
    record_date: date
    tax_identity: str | None
    net_amount: Decimal | None = None
    tax_amount: Decimal | None = None
    tax_rate: Decimal | None = None
    currency: str = "USD"
    sign: int = 1


@dataclass(frozen=True)
class BankRecord:
    """Represent bank-side financial settlement evidence."""

    record_id: str

    vendor_name: str | None
    reference: str | None
    amount: Decimal
    record_date: date
    currency: str = "USD"
    sign: int = -1
