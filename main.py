`from wand.image import Image
from google.cloud import storage

client = storage.Client()

THUMBNAIL_BUCKET = 'dsthumbnail_bucket'
bucket = 'devopssourav-bucket'

def make_thumbnail(data, context):
    # Get the file that has been uploaded to GCS
    bucket = client.get_bucket(data['bucket'])
    blob = bucket.get_blob(data['name'])
    imagedata = blob.download_as_string()
    # Create a new image object and resample it
    newimage = Image(blob=imagedata)
    newimage.sample(200,200)
    #Upload the resampled image to the other bucket
    bucket = client.get_bucket(THUMBNAIL_BUCKET)
    newblob = bucket.blob('thumbnail-' + data['name'])     
    newblob.upload_from_string(newimage.make_blob())

