
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
    default=False,
)
def main(env: str, debug: bool):
    os.environ["ENV"] = env
    os.environ["DEBUG"] = str(debug)
    # confirm dotenv is working
    print('OPENAI KEY', os.getenv("OPENAI_API_KEY"))
    uvicorn.run(
        app="app.server:app",
        # host=config.APP_HOST,
        # port=config.APP_PORT,
        # reload=True if config.ENV != "production" else False,
        workers=1,
    )


if __name__ == "__main__":
    main()
