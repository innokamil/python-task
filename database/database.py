import abc
import os
from pathlib import Path
from typing import Any,  Tuple, List
from dataclasses import dataclass
from tabulate import tabulate
from utils.writers import write_into_json, write_into_xml

@dataclass
class QueryResult:
    filename: str
    colnames: List[str] 
    records: List[Tuple]

    def __repr__(self) -> str:
        return tabulate(self.records, headers=self.colnames, tablefmt="grid")

    def write_into_json(self) -> bool:
        obj = list(map(lambda record: {
            k : v for k, v in zip(self.colnames, record)
        }, self.records))
        write_into_json(Path(os.getenv("RESOURCES_DIRECTORY"))/"dump"/self.filename,
                        obj)
        return True

    def write_into_xml(self) -> bool:
        obj = list(map(lambda record: {
            k : v for k, v in zip(self.colnames, record)
        }, self.records))
        write_into_xml(Path(os.getenv("RESOURCES_DIRECTORY"))/"dump"/self.filename,
                        obj)
        return True



@dataclass
class DatabaseCredentials:
    """
    Class for keeping a database connection information.
    """
    dbname: str
    port: str
    user: str
    password: str

    def __are_fields_valid(self) -> bool:
        """
        Check if fields are valid.

        Returns:
            True if fields are valid and can be used to construct a DSN string,
            otherwise False
        """
        return (
            len(self.dbname) != 0 and
            len(self.port) != 0 and
            len(self.user) != 0 and
            len(self.password) != 0
        )

    
    def into_dsn(self) -> str | None:
        """
        Construct a DSN from class fields.

        Returns:
            String in the DSN format if fields are valid, otherwise None that
            denotes a failure in constructing a DSN string.
        """
        return (
            f"dbname={self.dbname} "
                f"host=pgdb "
                f"port={self.port} "
                f"user={self.user} "
                f"password={self.password}"
        ) if self.__are_fields_valid() else None


class Database(abc.ABC):
    @abc.abstractmethod
    def _initialize_schema(self) -> None | bool:
        ...

    @abc.abstractmethod
    def select(self, stmt: str) -> QueryResult:
        ...

    @abc.abstractmethod
    def insert(self, stmt: str, items: Any):
        ...
