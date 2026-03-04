import subprocess

def test_app_runs():
    result = subprocess.run(["python", "/app/app.py"], capture_output=True)
    assert result.returncode == 0

