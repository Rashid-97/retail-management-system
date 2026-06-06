class AppError(Exception):
    status_code = 400
    detail = "Application error"

    def __init__(self, detail: str | None = None):
        self.detail = detail or self.detail


class DomainValidationError(AppError):
    status_code = 400
    detail = "Validation failed"


class BusinessRuleError(AppError):
    status_code = 400
    detail = "Business rule failed"


class DuplicateError(AppError):
    status_code = 409
    detail = "Duplicate error"


class DatabaseException(AppError):
    status_code = 500
    detail = "Database error"


class NotFoundException(AppError):
    status_code = 404
    detail = "Not found"
