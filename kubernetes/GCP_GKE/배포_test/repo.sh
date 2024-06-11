# PROJECT_ID == gcloud config get-value project 명령어로 확인
gcloud artifacts repositories create hello-repo \
    --project=[PROJECT_ID] \
    --repository-format=docker \
    --location=us-central1 \
    --description="Docker repository"