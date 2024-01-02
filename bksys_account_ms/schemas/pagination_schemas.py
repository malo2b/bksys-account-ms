"""The pagination, input and output models with helper structures."""
import math

from pydantic import Field

from .common_schemas import CamelCaseBaseModel


class Pagination(CamelCaseBaseModel):
    """A description of the pagination status in paginated route responses."""

    page_index: int
    results_per_page: int
    total_pages: int
    total_results: int


class Paginated(CamelCaseBaseModel):
    """Pagination parameters for paginated routes."""

    page_index: int = Field(0, ge=0)
    per_page: int = Field(50, ge=1, le=100)

    @property
    def limit(self) -> int:
        """Get the `limit` to set in the SQL query."""
        return self.per_page

    @property
    def offset(self) -> int:
        """Get the `offset` to set in the SQL query."""
        return self.page_index * self.per_page

    def with_total(self, total: int) -> Pagination:
        """Compute the return pagination model from the input and the total."""
        return Pagination.model_construct(
            page_index=self.page_index,
            results_per_page=self.per_page,
            total_results=total,
            total_pages=math.ceil(total / self.per_page),
        )


__all__ = ["Pagination", "Paginated"]
