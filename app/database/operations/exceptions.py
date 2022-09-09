class DatabaseOperationException(Exception):
    """Database Operation error."""


class DatabaseNotFoundException(DatabaseOperationException):
    """Thrown when an entity is not found"""
