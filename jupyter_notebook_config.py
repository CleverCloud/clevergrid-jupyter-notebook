import os
from s3contents import S3ContentsManager



TOKEN = os.getenv("TOKEN", None)
PASSWORD = os.getenv("PASSWORD", None)

CELLAR_ADDON_KEY_ID = os.getenv("CELLAR_ADDON_KEY_ID")
CELLAR_ADDON_KEY_SECRET = os.getenv("CELLAR_ADDON_KEY_SECRET")
BUCKET_NOTEBOOK_NAME = os.getenv("BUCKET_NOTEBOOK_NAME")
CELLAR_ADDON_HOST = os.getenv("CELLAR_ADDON_HOST")

APP_ID = os.getenv("APP_ID")

c = get_config()

# Custom base url
c.NotebookApp.custom_display_url = "http://app-" + APP_ID[len("app_"):] + ".cleverapps.io"

# Tell Jupyter to use S3ContentsManager for all storage.
c.NotebookApp.contents_manager_class = S3ContentsManager
c.S3ContentsManager.access_key_id = CELLAR_ADDON_KEY_ID
c.S3ContentsManager.secret_access_key = CELLAR_ADDON_KEY_SECRET
c.S3ContentsManager.bucket = BUCKET_NOTEBOOK_NAME
c.S3ContentsManager.endpoint_url = "https://" + CELLAR_ADDON_HOST

if TOKEN is not None:
    c.NotebookApp.token = TOKEN
if PASSWORD is not None:
    c.NotebookApp.password = PASSWORD

# Optional settings:
c.S3ContentsManager.prefix = ""
