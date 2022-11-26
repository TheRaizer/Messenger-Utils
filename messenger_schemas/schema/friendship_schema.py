from __future__ import annotations

from sqlalchemy import (
    Column,
    DATETIME,
    ForeignKeyConstraint,
    Integer,
    PrimaryKeyConstraint,
)
from sqlalchemy.orm import relationship
from .friendship_status_schema import FriendshipStatusSchema
from ..schema import Base, BaseRecord
from typing import TYPE_CHECKING, Any, List

if TYPE_CHECKING:
    from .user_schema import UserSchema


class FriendshipSchema(Base, BaseRecord):
    __tablename__ = "friendship"
    requester_id = Column(Integer, nullable=False)
    addressee_id = Column(Integer, nullable=False)
    created_date_time = Column(DATETIME, nullable=False)

    PrimaryKeyConstraint(requester_id, addressee_id)

    ForeignKeyConstraint(
        [requester_id],
        ["user.user_id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
        name="friendship_requester_id_FK",
    )

    ForeignKeyConstraint(
        [addressee_id],
        ["user.user_id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
        name="friendship_addressee_id_FK",
    )

    requester: UserSchema = relationship(
        "UserSchema", foreign_keys=[requester_id], back_populates="friend_requests_sent"
    )
    addressee: UserSchema = relationship(
        "UserSchema",
        foreign_keys=[addressee_id],
        back_populates="friend_requests_recieved",
    )
    statuses: List[FriendshipStatusSchema] = relationship(
        FriendshipStatusSchema.__name__,
        foreign_keys=[
            FriendshipStatusSchema.addressee_id,
            FriendshipStatusSchema.requester_id,
        ],
    )

    def key(self) -> Any:
        return (self.requester_id, self.addressee_id)
