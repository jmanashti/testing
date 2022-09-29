gcloud builds submit --tag gcr.io/rankstrategy-ce64c/socialnetworks  --project=rankstrategy-ce64c

gcloud run deploy socialnetworks --image gcr.io/rankstrategy-ce64c/socialnetworks --platform managed  --project=rankstrategy-ce64c --allow-unauthenticated --region us-east1

gcloud iam service-accounts list --project=rankstrategy-ce64c

gcloud iam service-accounts keys create ./keys.json --iam-account  github-action@rankstrategy-ce64c.iam.gserviceaccount.com

gcloud auth activate-service-account --key-file=keys.json

# Useful links
* Paul Craig [blog](https://dev.to/pcraig3/quickstart-continuous-deployment-to-google-cloud-run-using-github-actions-fna)
* GitHub action [deploy-cloudrun](https://github.com/google-github-actions/deploy-cloudrun)
* Cloud Run simple Flask application [tutorial](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/python)
* [Installing Google Cloud SDK](https://cloud.google.com/sdk/docs/install)