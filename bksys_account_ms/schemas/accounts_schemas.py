"""Accounts schemas."""

from pydantic import Field
from .common_schemas import CamelCaseBaseModel
from .pagination_schemas import Pagination


class Account(CamelCaseBaseModel):
    """Account schema."""

    account_id: int = Field()
    user_id: int = Field()
    account_type: str = Field()
    account_number: int = Field()
    balance: float = Field()


class AccountResponse(CamelCaseBaseModel):
    """Account response schema."""

    data: Account


class PaginatedAccountResponse(CamelCaseBaseModel):
    """Paginated account response schema."""

    data: list[Account]
    pagination: Pagination


__all__ = ["Account", "AccountResponse", "PaginatedAccountResponse"]
