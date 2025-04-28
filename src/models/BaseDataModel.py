from helpers.config import get_settings, Settings

class BaseDataModel:
    """
    A base data model class to manage database connections and application settings.
    This can be extended by specific models to interact with different databases.
    """

    def __init__(self, db_client: object):
        """
        Initializes the BaseDataModel instance with the provided database client and application settings.

        Args:
            db_client (object): The database client object (e.g., MongoDB, SQLAlchemy, etc.).
        """
        self.db_client = db_client
        self.app_settings = get_settings()

    def get_database(self, db_name: str):
        """
        Retrieves the specified database from the database client.

        Args:
            db_name (str): The name of the database to retrieve.

        Returns:
            Database: The requested database object.
        """
        # Assuming db_client is a MongoClient or similar
        return self.db_client[db_name]

    def get_settings(self) -> Settings:
        """
        Retrieves the application settings.

        Returns:
            Settings: The application settings object.
        """
        return self.app_settings
