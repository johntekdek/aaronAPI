import pytest
import sys
sys.path.append('aaronAPI')
from todoserver import app
import json

def test_response():
    client = app.test_client()
    resp = client.get('/')    
    assert 200 == resp.status_code
    
def test_empty_list_of_tasks():
    client = app.test_client()
    resp = client.get('/tasks/')    
    data = json.loads(resp.data.decode("utf-8"))
    assert data == []