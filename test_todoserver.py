import pytest
import sys
sys.path.append('aaronAPI')
from todoserver import app

def test_empty_list_of_tasks():
    client = app.test_client()
    resp = client.get('/tasks/')    
    assert 'Hello' == resp.get_data()
    assert 201 == resp.status_code
