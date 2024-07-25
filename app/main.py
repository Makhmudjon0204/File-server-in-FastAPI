from fastapi import FastAPI
from app.routers import (
    news,
    groups, 
    members,
    member_info,
    member_groups,
    blogs,
    projects,
    courses,
    service_groups,
    services,
    group_services
)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "TQQT project is working!"}

app.include_router(news.router, prefix="/news", tags=["news"])
app.include_router(groups.router, prefix="/groups", tags=["groups"])
app.include_router(members.router, prefix="/members", tags=["members"])
app.include_router(member_info.router, prefix="/member_info", tags=["member_info"])
app.include_router(member_groups.router, prefix="/group_members", tags=["group_members"])
app.include_router(projects.router, prefix="/projects", tags=["projects"])
app.include_router(blogs.router, prefix="/blogs", tags=["blogs"])
app.include_router(courses.router, prefix="/courses", tags=["courses"])
app.include_router(service_groups.router, prefix="/service_groups", tags=["service_groups"])
app.include_router(services.router, prefix="/services", tags=["services"])
app.include_router(group_services.router, prefix="/group_services", tags=["group_services"])