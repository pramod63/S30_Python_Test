# S30_Python_Test
FastAPI task

# Initial command to create and activate virtual env
mkdir mytodo
cd mytodo
virtualenv virtualenv_folder # To create virtual env
virtualenv_folder\Scripts\activate

## Install required packages

pip install fastapi uvicorn jinja2 python-multipart

## Install database connection in env
pip install databases


## To Run the application in local machine
uvicorn main:app --reload

## Built-in FastAPI’s Swagger Doc
http://localhost:8000/docs
http://localhost:8000/redoc

## Find the sample input data in the below link
https://github.com/pramod63/S30_Python_Test/blob/Test_Phase1/sampleData.txt



## Reference

## Database connection
https://fastapi.tiangolo.com/tutorial/sql-databases/

## To calculate the distance btw lat and long of 2 places
https://www.geeksforgeeks.org/program-distance-two-points-earth/
