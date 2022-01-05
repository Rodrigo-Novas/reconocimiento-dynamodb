import boto3
from botocore.exceptions import ClientError
import json

URL = "HTTP://LOCALHOST:8000"
AWS_ACCESS_KEY_ID = "DUMMYIDEXAMPLE"
AWS_SECRET_ACCESS_KEY = "DUMMYEXAMPLEKEY"

# Defino y creo una tabla
def create_table(DynamoDB=None, Session=None): 
    if not Session:
        # Crea una sesion
        Session = boto3.session.Session(aws_access_key_id= AWS_ACCESS_KEY_ID, aws_secret_access_key = AWS_SECRET_ACCESS_KEY)
        # instancio DynamoDB
        DynamoDB = Session.resource("dynamodb", region_name='sa-east-1', endpoint_url=URL)
        
        GamingTABLE = DynamoDB.create_table(
            TableName='CallOfDuty',
            AttributeDefinitions=[
            {
                "AttributeName":"GamerTag",
                "AttributeType": "S" #string
            },
            {
                "AttributeName":"MatchMode",
                "AttributeType":"S" #string
            }
            ],
            KeySchema=[
                
            {
                "AttributeName":"GamerTag",
                "KeyType": "HASH" # el hash es el partition key
            },
            {
                "AttributeName":"MatchMode",
                "KeyType": "RANGE" # el range es el order id
            }
            ],
            ProvisionedThroughput={
                "ReadCapacityUnits": 100,
                "WriteCapacityUnits": 100
            }
        )
        return GamingTABLE

def insert_items(DynamoDB=None, Session=None): 
    if not Session:
        # Crea una sesion
        Session = boto3.session.Session(aws_access_key_id= AWS_ACCESS_KEY_ID, aws_secret_access_key = AWS_SECRET_ACCESS_KEY)
        # instancio DynamoDB
        DynamoDB = Session.resource("dynamodb", region_name='sa-east-1', endpoint_url=URL)
        GamingTable = DynamoDB.Table("CallOfDuty")
        GamingTable.put_item(
            Item={
                "GamerTag":"1236",
                "MatchMode": "BR"
            }
        )
        GamingTable.put_item(
            Item={
                "GamerTag":"1236",
                "MatchMode": "BR",
                "Kills":25,
                "Win":False,
                "TeamMates":["gamer36", "gamer78", "gamer65"]

            }
        )




if __name__ == "__main__":
    # games = create_table()
    # print(games.table_status)
    print(insert_items())