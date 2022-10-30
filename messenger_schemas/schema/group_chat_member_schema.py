from sqlalchemy import Column, ForeignKeyConstraint, Integer, PrimaryKeyConstraint
from ..schema import Base

class GroupChatMemberSchema(Base):
    __tablename__ = "group_chat_member"
    group_chat_id = Column(Integer, nullable=False)
    member_id = Column(Integer, nullable=False)
    
    PrimaryKeyConstraint(group_chat_id, member_id)
    
    ForeignKeyConstraint([group_chat_id], ["group_chat.group_chat_id"], 
                        onupdate="CASCADE", ondelete="CASCADE",
                        name="group_chat_member_group_chat_id_FK")
    ForeignKeyConstraint([member_id], ["user.user_id"], 
                        onupdate="CASCADE", ondelete="CASCADE",
                        name="group_chat_member_member_id_FK")