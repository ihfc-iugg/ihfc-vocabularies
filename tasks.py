import datetime
import os

from invoke import task


@task
def check(c):
    """
    Check the consistency of the project using various tools
    """
    print("🚀 Checking Poetry lock file consistency with 'pyproject.toml': Running poetry lock --check")
    c.run("poetry lock --check")

    print("🚀 Linting code: Running pre-commit")
    c.run("poetry run pre-commit run -a")

    print("🚀 Static type checking: Running mypy")
    c.run("poetry run mypy")

    print("🚀 Checking for obsolete dependencies: Running deptry")
    c.run("poetry run deptry .")


@task
def test(c, tox=False):
    """
    Run the test suite
    """
    if tox:
        print("🚀 Testing code: Running pytest with all tests")
        c.run("tox")
    else:
        print("🚀 Testing code: Running pytest")
        c.run("poetry run pytest --cov --cov-config=pyproject.toml --cov-report=html")


@task
def docs(c, live=False):
    """
    Build the documentation and open it in the browser
    """
    if live:
        # fmt: off
        command = ("sphinx-autobuild docs/ docs/_build"
                        " -E"
                        # " -c ."
                        " --host 127.0.0.1"
                        " --port 0"
                        " --watch ."
            )
        # fmt: on
    else:
        command = "sphinx-build docs/ docs/_build -E"
    c.run(command)


@task
def release(c):
    """
    Create a new release using year.release-number versioning.
    """
    # 1. Determine the current year
    current_year = datetime.datetime.now().year

    # 2. Get the latest tag to find the current release number
    result = c.run(
        "git tag --list 'v{}.*' --sort=-v:refname".format(current_year),
        hide=True,
        warn=True,
    )
    tags = result.stdout.strip().splitlines()

    if tags:
        # Extract the highest release number for the current year
        latest_tag = tags[0]
        latest_release_number = int(latest_tag.split(".")[1])
        new_release_number = latest_release_number + 1
    else:
        # First release of the year
        new_release_number = 1

    # 3. Form the new version string
    new_version = f"{current_year}.{new_release_number}"

    # 4. Update the version in pyproject.toml
    c.run(f"poetry version {new_version}")

    # 5. Commit the change
    # c.run(f'git commit pyproject.toml -m "bump to v{new_version}"')

    # 6. Create a tag and push it
    # c.run(f'git tag -a v{new_version} -m "Release {new_version}"')
    # c.run("git push --tags")
    # c.run("git push origin main")


@task
def new_translation(c, lang):
    """Creates a new translation file for the specified language.

        lang (str): The language code for the new translation.

    Raises:
        OSError: If the locale directory cannot be created.
    """
    if not os.path.exists("locale"):
        os.makedirs("locale")
    locale_dir = "locale"

    c.run(f"pybabel extract -o {locale_dir}/messages.pot .")
    c.run(f"pybabel init -i {locale_dir}/messages.pot -d {locale_dir} -l {lang}")

@task
def update_translations(c):
    """Updates all existing translation files with new extracted messages.

    """
    locale_dir = "locale"
    c.run(f"pybabel update -i {locale_dir}/messages.pot -d {locale_dir}")

@task
def compile_translations(c):
    """Compiles all translation files into binary format for use.

    """
    locale_dir = "locale"
    c.run(f"pybabel compile -d {locale_dir}")

@task
def build(c, format="turtle"):
    """Builds vocabularies in the specified format.

    Args:
        format (str, optional): The format in which to export vocabularies. Defaults to "turtle".

    Raises:
        ImportError: If `skos_builder.utils` is not installed.
    """
    from skos_builder.utils import export_vocabs

    export_vocabs("src.vocabularies", "data")
