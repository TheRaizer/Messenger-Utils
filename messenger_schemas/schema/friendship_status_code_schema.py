from typing import Any
from sqlalchemy import (
    CHAR,
    Column,
    VARCHAR,
    PrimaryKeyConstraint,
    UniqueConstraint,
)
from ..schema import BaseRecord, Base


class FriendshipStatusCodeSchema(Base, BaseRecord):
    __tablename__ = "friendship_status_code"
    status_code_id = Column(CHAR(1), nullable=False)
    name = Column(VARCHAR(20), nullable=False)

    UniqueConstraint(status_code_id)
    UniqueConstraint(name)

    PrimaryKeyConstraint(status_code_id, name)

    def key(self) -> Any:
        return (self.status_code_id, self.name)
