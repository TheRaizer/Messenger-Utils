from typing import Any
from sqlalchemy import (
    CHAR,
    DATETIME,
    Column,
    ForeignKeyConstraint,
    Integer,
    PrimaryKeyConstraint,
)
from sqlalchemy.orm import relationship
from .friendship_status_code_schema import FriendshipStatusCodeSchema
from ..schema import BaseRecord, Base


class FriendshipStatusSchema(Base, BaseRecord):
    __tablename__ = "friendship_status"
    requester_id = Column(Integer, nullable=False)
    addressee_id = Column(Integer, nullable=False)
    specified_date_time = Column(DATETIME, nullable=False)
    status_code_id = Column(CHAR(1), nullable=False, server_default="R")
    specifier_id = Column(Integer, nullable=False)

    PrimaryKeyConstraint(requester_id, addressee_id, specified_date_time)

    ForeignKeyConstraint(
        [requester_id, addressee_id],
        ["friendship.requester_id", "friendship.addressee_id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
        name="friendship_status_friend_id_FK",
    )

    ForeignKeyConstraint(
        [status_code_id],
        ["friendship_status_code.status_code_id"],
        onupdate="CASCADE",
        ondelete="SET DEFAULT",
        name="friendship_status_status_code_id_FK",
    )

    ForeignKeyConstraint(
        [specifier_id],
        ["user.user_id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
        name="friendship_status_specifier_id_FK",
    )

    status_code: FriendshipStatusCodeSchema = relationship(
        FriendshipStatusCodeSchema.__name__
    )

    def key(self) -> Any:
        return (self.requester_id, self.addressee_id, self.specified_date_time)
