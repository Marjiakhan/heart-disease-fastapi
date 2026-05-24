from pydantic import BaseModel, Field

class HeartData(BaseModel):

    age: int = Field(..., example=63)
    sex: int = Field(..., example=1)
    cp: int = Field(..., example=3)
    trestbps: int = Field(..., example=145)
    chol: int = Field(..., example=233)
    fbs: int = Field(..., example=1)
    restecg: int = Field(..., example=0)
    thalach: int = Field(..., example=150)
    exang: int = Field(..., example=0)
    oldpeak: float = Field(..., example=2.3)
    slope: int = Field(..., example=0)
    ca: int = Field(..., example=0)
    thal: int = Field(..., example=1)