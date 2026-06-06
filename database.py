from sqlmodel import create_engine
import sqlmodel 


file_name="bosss.db"
url_bd=f"sqlite:///{file_name}"


engine= create_engine(
    
    url_bd,
    echo=True,
    connect_args={"check_same_thread":
    False}
)


