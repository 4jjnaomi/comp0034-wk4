import os
from pathlib import Path
import pytest
from paralympics import create_app, db


@pytest.fixture(scope='module')
def app():
    """Fixture that creates a test app.

    The app is created with test config parameters that include a temporary database. The app is created once for
    each test module.

    Returns:
        app A Flask app with a test config
    """
    # Location for the temporary testing database
    db_path = Path(__file__).parent.parent.joinpath('data', 'paralympics_testdb.sqlite')
    test_cfg = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///" + str(db_path),
    }
    app = create_app(test_config=test_cfg)

    # # Push an application context to bind the SQLAlchemy object to the application
    with app.app_context():
        db.create_all()

    yield app

    # # Clean up / reset resources
    with app.app_context():
        db.session.remove()  # Close the database session
        db.drop_all()

        # Explicitly close the database connection
        db.engine.dispose()

    # Delete the test database
    os.unlink(db_path)
    


@pytest.fixture()
def client(app):
    return app.test_client()