from invoke import task
import platform

os = platform.system()

pty_arvo = True
python = "python3"
if os == "Windows":
    pty_arvo = False
    python = "python"

@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src", pty=pty_arvo)
    
@task
def lint(ctx):
    ctx.run("pylint src", pty=pty_arvo)
    
@task
def start(ctx):
    ctx.run(f"{python} src/index.py", pty=pty_arvo)
    

@task
def build(ctx):
    ctx.run(f"{python} src/build.py", pty=pty_arvo)
    
@task
def test(ctx):
    ctx.run("pytest src/", pty=pty_arvo)
    
@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=pty_arvo)
    
@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=pty_arvo)
    