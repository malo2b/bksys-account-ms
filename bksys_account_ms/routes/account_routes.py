"""Accounts routes."""

import logging
from fastapi import APIRouter, Depends, status

from ..schemas.accounts_schemas import AccountResponse, PaginatedAccountResponse
from ..services.accounts_service import AccountsService
from ..helpers.response import HTTPResponse
from ..schemas.pagination_schemas import Paginated

log = logging.getLogger(__name__)


router = APIRouter(prefix="/accounts")


@router.get("/", tags=["Accounts"])
async def get_accounts(
    paginated: Paginated = Depends(), service: AccountsService = Depends()
) -> PaginatedAccountResponse:
    return HTTPResponse(status.HTTP_200_OK, await service.get_accounts(paginated))


@router.get("/{account_id}", tags=["Accounts"])
async def get_account(
    account_id: int, service: AccountsService = Depends()
) -> AccountResponse:
    return HTTPResponse(status.HTTP_200_OK, await service.get_account(account_id))
