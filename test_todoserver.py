import pytest
import sys
sys.path.append('aaronAPI')
from todoserver import app
import json
app.testing =True

def test_response():
    client = app.test_client()
    resp = client.get('/')    
    assert 200 == resp.status_code
    assert b'Hello World !' == resp.data
    
def test_empty_list_of_tasks():
    client = app.test_client()
    resp = client.get('/tasks/')    
    data = json.loads(resp.data.decode("utf-8"))
    assert data == []

def test_create_a_task_and_get_its_details():
    # arrange 
    client = app.test_client()
    resp = client.get("/tasks/")
    data = json.loads(resp.data.decode("utf-8"))    
    # action
    new_task_data = {
        "summary":"get milk",
        "desc": "one gallon of milk"
    }
    resp = client.post("/tasks/", data = json.dumps(new_task_data),follow_redirects=True)
    assert 201 == resp.status_code
    data = json.loads(resp.data.decode("utf-8"))
    assert 'id' in data

