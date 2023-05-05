from invoke import task

@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src", pty=True)
    
@task
def lint(ctx):
    ctx.run("pylint src", pty=True)
    
@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)
    

@task
def build(ctx):
    ctx.run("python3 src/build", pty=True)
    
@task
def test(ctx):
    ctx.run("pytest -s src/", pty=True)
    
@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)
    
@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)
    
  
C:\Users\aarni\AppData\Local\Programs\Python\Python310\Scripts
%APPDATA%\Python\Scripts