from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.connection import get_db
from models.profile import UserProfile
from models.user import User
from schemas.profile import ProfileCreate, ProfileResponse, ProfileUpdate

router = APIRouter(prefix="/profiles", tags=["Profile Management"])

@router.post("/", response_model=ProfileResponse, status_code=status.HTTP_201_CREATED)
def create_profile(profile_data: ProfileCreate, db: Session = Depends(get_db)):
    # Check if user exists
    user = db.query(User).filter(User.id == profile_data.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Check if profile already exists
    existing_profile = db.query(UserProfile).filter(UserProfile.user_id == profile_data.user_id).first()
    if existing_profile:
        raise HTTPException(status_code=400, detail="Profile already exists for this user")
        
    new_profile = UserProfile(**profile_data.model_dump())
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    return new_profile

@router.get("/{user_id}", response_model=ProfileResponse)
def get_profile_by_user_id(user_id: int, db: Session = Depends(get_db)):
    profile = db.query(UserProfile).filter(UserProfile.user_id == user_id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile

@router.put("/{user_id}", response_model=ProfileResponse)
def update_profile(user_id: int, update_data: ProfileUpdate, db: Session = Depends(get_db)):
    profile = db.query(UserProfile).filter(UserProfile.user_id == user_id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
        
    for key, value in update_data.model_dump(exclude_unset=True).items():
        setattr(profile, key, value)
        
    db.commit()
    db.refresh(profile)
    return profile

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_profile(user_id: int, db: Session = Depends(get_db)):
    profile = db.query(UserProfile).filter(UserProfile.user_id == user_id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    db.delete(profile)
    db.commit()
    return None