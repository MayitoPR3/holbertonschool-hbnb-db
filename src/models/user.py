
from flask_bcrypt import Bcrypt
from app import db

bcrypt = Bcrypt()

class User(db.Model):
    """User representation"""
    
    __tablename__ = 'users'
    
    # id = db.Column(db.Integer, primary_key=True)
    # created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    # updated_at = db.Column(db.DateTime, onupdate=db.func.current_timestamp())
    
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    
    
    # def set_password(self, password):
    #     self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        
    # def check_password(self, password):
    #     return bcrypt.check_password_hash(self.password_hash, password)

    def __init__(self, email: str, password: str, first_name: str, last_name: str, is_admin=False, **kwargs):
        super().__init__(**kwargs)
        self.email = email
        self.password = password
        #self.set_password(password)
        self.is_admin = is_admin
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"<User {self.id} ({self.email})>"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "is_admin": self.is_admin,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def create(user_data: dict) -> "User":
        from src.persistence import repo
        """Create a new user"""
        email = user_data.get("email")
        # existing_user = User.query.filter_by(email=email).first()
        users: list["User"] = User.get_all()
        
        # print("Hello im inside the create")
        print(f"The user data inde the create ------{user_data} ------")
        # for user in users:
        #     if user.email == user_data.get("email"):
        #         raise ValueError("User already exists")

        new_user = User(**user_data)
        # db.session.add(new_user)
        # db.session.commit()
        repo.save(new_user)

        return new_user

    @staticmethod
    def update(user_id: int, data: dict) -> "User | None":
        """Update an existing user"""
        user = User.query.get(user_id)

        if not user:
            return None

        if "email" in data:
            user.email = data["email"]
        if "first_name" in data:
            user.first_name = data["first_name"]
        if "last_name" in data:
            user.last_name = data["last_name"]

        db.session.commit()

        return user
