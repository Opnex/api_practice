from fastapi import FastAPI
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()

app = FastAPI(title="Simple FastAPI App", version="1.0.0")

@app.get("/get-student-details")
def get_student_details():
    return {
        "Students Details": [
            {
                "Name": "Ayobami Iretioluwa",
                "Age": "20",
                "Sex": "Male",
                "City": "Lagos",
                "Track": "AI Developer"
            },
            {
                "Name": "Iremide Olayinka",
                "Age": "15",
                "Sex": "Female",
                "City": "Abuja",
                "Track": "AI Engineer"
            },
            {
                "Name": "Oloruntola Tunde",
                "Age": "25",
                "Sex": "Male",
                "City": "Ibadan",
                "Track": "AI Developer"
            },
            {
                "Name": "Boluwatife Opemipo",
                "Age": "18",
                "Sex": "Female",
                "City": "Abeokuta",
                "Track": "AI Engineer"
            },
            {
                "Name": "Stephen Peter",
                "Age": "22",
                "Sex": "Male",
                "City": "Osogbo",
                "Track": "AI Developer"
            }
        ]
    }

if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port")))