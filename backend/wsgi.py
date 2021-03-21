from application import db, init_app

app = init_app()


@app.cli.command("create-all")
def create_all():
    db.create_all()


@app.cli.command("drop-all")
def drop_all():
    db.drop_all()


@app.cli.command("urls")
def url_map():
    print(app.url_map)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
