from invoke import task

@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src", pty=True)
    
def start(ctx):
    pass
    
@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)
    
@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)
