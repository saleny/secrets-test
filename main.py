from fastapi import FastAPI
from app.core.config import settings
from app.routers import auth, users, projects, scans
from app.database import engine, SessionLocal
from app.models.base import Base
from app.models.user import User
from app.utils.security import get_password_hash
from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
)

app.include_router(auth.router, prefix="/api/auth")
app.include_router(users.router, prefix="/api/users")
app.include_router(projects.router, prefix="/api/projects")
app.include_router(scans.router, prefix="/api/scans")



@app.on_event("startup")
def create_admin_user():
    with SessionLocal() as db:
        try:
            admin = db.query(User).filter(User.username == "admin").first()
            if not admin:
                hashed_password = get_password_hash("admin")
                admin_user = User(
                    username="admin",
                    hashed_password=hashed_password,
                    is_admin=True,
                    disabled=False,
                )
                db.add(admin_user)
                db.commit()
                print("✅ Admin user created successfully")
            else:
                print("ℹ️ Admin user already exists")
        except Exception as e:
            db.rollback()
            print(f"❌ Error creating admin user: {e}")
        finally:
            db.close()

@app.get("/")
async def root():
    return {"message": "Secret Scanner API"}

