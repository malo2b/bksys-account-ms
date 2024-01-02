from aiomysql import DictCursor
from fastapi import Depends, HTTPException

from ..database import get_db
from ..schemas import Paginated, PaginatedAccountResponse, AccountResponse, Account


class AccountsService:
    """Accounts service."""

    def __init__(self, db=Depends(get_db)) -> None:
        self.db: DictCursor = db

    async def get_accounts(self, paginated: Paginated) -> PaginatedAccountResponse:
        """Get accounts."""
        query: str = """
            SELECT
                a.idAccount as account_id,
                a.idUser as user_id,
                acc_type.typeName as account_type,
                a.accountNumber as account_number,
                balance,
                COUNT(*) OVER() as total_count
            FROM
                Account a
            INNER JOIN AccountType acc_type on
                acc_type.idAccountType = a.idAccountType
            ORDER BY idAccount DESC
            LIMIT %s OFFSET %s
            """
        params: tuple[int, int] = (paginated.limit, paginated.offset)
        async with self.db.cursor(DictCursor) as cursor:
            await cursor.execute(query, params)
            result = await cursor.fetchall()

        if result:
            return PaginatedAccountResponse(
                data=[Account(**row) for row in result],
                pagination=paginated.with_total(result[0]["total_count"]),
            )
        raise HTTPException(
            status_code=404, detail="No accounts found for this request."
        )

    async def get_account(self, account_id: str) -> AccountResponse:
        query: str = """
            SELECT
                a.idAccount as account_id,
                a.idUser as user_id,
                acc_type.typeName as account_type,
                a.accountNumber as account_number,
                balance,
                COUNT(*) OVER() as total_count
            FROM
                Account a
            INNER JOIN AccountType acc_type on
                acc_type.idAccountType = a.idAccountType
            WHERE
                a.idAccount = %s
            """
        params: tuple[int] = (account_id,)
        async with self.db.cursor(DictCursor) as cursor:
            await cursor.execute(query, params)
            result = await cursor.fetchall()

        if result:
            return AccountResponse(data=Account(**result[0]))
        raise HTTPException(
            status_code=404,
            detail=f"No account found for this account_id `{account_id}`.",
        )


__all__ = ["AccountsService"]
