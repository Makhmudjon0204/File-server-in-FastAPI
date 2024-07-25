from database import Base, engine
from models.blogs import Blogs
from models.courses import Courses
from models.group_services import GroupServices
from models.groups import Groups
from models.member_groups import MemberGroup
from models.member_info import MemberInfo
from models.members import Members
from models.news import News
from models.projects import Projects
from models.service_groups import ServiceGroup
from models.services import Services


Base.metadata.create_all(bind=engine)