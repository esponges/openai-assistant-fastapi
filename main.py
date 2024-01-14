import os
import click
import uvicorn

from dotenv import load_dotenv

load_dotenv()

@click.command()
@click.option(
    "--env",
    type=click.Choice(["local", "dev", "prod"], case_sensitive=False),
    default="local",
)
@click.option(
    "--debug",
    type=click.BOOL,
    is_flag=True,
    default=True,
)
def main(env: str, debug: bool):
    os.environ["ENV"] = env
    os.environ["DEBUG"] = str(debug)
    print("ENV", os.getenv("ENV"))
    print("DEBUG", os.getenv("DEBUG"))
    uvicorn.run(
        app="app.server:app",
        # host=config.APP_HOST,
        # port=config.APP_PORT,
        reload= env != "prod",
        workers=1,
    )


if __name__ == "__main__":
    main() # pylint: disable=no-value-for-parameter
