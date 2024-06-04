# 영구 스토리지 생성
# project_id 확인
gcloud projects list
gcloud compute disks create --size=10Gi --zone=us-central1-c mongodb --project=[projectName]
