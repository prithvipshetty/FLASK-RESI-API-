# import requests

# BASE = "http://127.0.0.1:5000/"

# response = requests.patch(BASE + "video/2", {})
# print(response.json())


import requests

BASE = "http://127.0.0.1:5000/"

# Ensure the database is in a clean state by deleting videos if they exist
for i in range(1, 4):
    response = requests.delete(BASE + f"video/{i}")
    if response.status_code == 200 or response.status_code == 204:
        print(f"Deleted video with ID {i}")

# Add a few videos
video_data = [
    {"name": "Video 1", "views": 100, "likes": 10},
    {"name": "Video 2", "views": 200, "likes": 20},
    {"name": "Video 3", "views": 300, "likes": 30},
]

for i in range(len(video_data)):
    response = requests.put(BASE + f"video/{i+1}", video_data[i])
    print(response.json())

# Update video 2
update_data = {"name": "Updated Video 2", "views": 250, "likes": 25}
response = requests.patch(BASE + "video/2", update_data)
print("Update Video 2 response:", response.json())

# Verify update by fetching video 2
response = requests.get(BASE + "video/2")
print("Get Updated Video 2 response:", response.json())

# Delete video 2
response = requests.delete(BASE + "video/2")
print("Delete Video 2 response:", response.status_code)

# Verify deletion by attempting to fetch video 2
response = requests.get(BASE + "video/2")
print("Get Deleted Video 2 response:", response.json() if response.status_code == 200 else response.status_code)
