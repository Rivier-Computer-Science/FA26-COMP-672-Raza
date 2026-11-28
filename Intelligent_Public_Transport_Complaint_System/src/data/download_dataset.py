
from pathlib import Path
from huggingface_hub import snapshot_download

# Find the project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Download destination
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

DATASET_ID = "faizmubeen/indian_railways_complaint_tweets"

def download_dataset():
    print("Starting dataset download...")

    downloaded_path = snapshot_download(
        repo_id=DATASET_ID,
        repo_type="dataset",
        local_dir=str(RAW_DATA_DIR)
    )

    print("\nDataset downloaded successfully!")
    print("Saved location:", downloaded_path)

if __name__ == "__main__":
    download_dataset()
