import cv2
import face_recognition
import os
from datetime import datetime
import shutil

reference_image_path = 'assets/perp.jpg'
reference_image = face_recognition.load_image_file(reference_image_path)
reference_face_encoding = face_recognition.face_encodings(reference_image)[0]

video_path = 'assets/Cam1.mp4'
cap = cv2.VideoCapture(video_path)

output_directory = 'output_faces'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

timestamps_with_matches = []

def crop_and_save_faces(frame, face_locations, output_directory, frame_count, timestamps):
    for i, face_location in enumerate(face_locations):
        top, right, bottom, left = face_location
        face_image = frame[top:bottom, left:right]
        cv2.imwrite(os.path.join(output_directory, f"face_{frame_count}_{i}.jpg"), face_image)
        timestamps.append(get_timestamp_from_frame(cap, frame_count))

def compare_faces_with_reference(output_directory, reference_face_encoding, timestamps):
    for filename in os.listdir(output_directory):
        if filename.endswith(".jpg"):
            face_image_path = os.path.join(output_directory, filename)
            face_image = face_recognition.load_image_file(face_image_path)
            face_encoding = face_recognition.face_encodings(face_image)

            if len(face_encoding) > 0 and face_recognition.compare_faces([reference_face_encoding], face_encoding[0])[0]:
                print(f"Match found! Face in {filename} matches the reference face.")
            else:
                print(f"No match found for {filename}.")

def get_timestamp_from_frame(cap, frame_number):
    fps = cap.get(cv2.CAP_PROP_FPS)
    timestamp_seconds = frame_number / fps
    timestamp = str(datetime.utcfromtimestamp(timestamp_seconds).strftime('%H:%M:%S'))
    return timestamp

skip_factor = 30

frame_count = 1
while True:
    ret, frame = cap.read()
    if not ret:
        break

    if frame_count % skip_factor == 0:
        face_locations = face_recognition.face_locations(frame)

        crop_and_save_faces(frame, face_locations, output_directory, frame_count, timestamps_with_matches)

    frame_count += 1

compare_faces_with_reference(output_directory, reference_face_encoding, timestamps_with_matches)

sorted_timestamps = sorted(timestamps_with_matches)

output_video_path = 'output_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter(output_video_path, fourcc, 3.0, (int(cap.get(3)), int(cap.get(4))))

for timestamp in sorted_timestamps:
    frame_number = int(timestamp.split(':')[-1]) * int(cap.get(cv2.CAP_PROP_FPS))
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    ret, frame = cap.read()
    output_video.write(frame)

output_video.release()
cap.release()
cv2.destroyAllWindows()

print("Sorted Timestamps:")
for timestamp in sorted_timestamps:
    print(timestamp)

print(f"Output Video Path: {output_video_path}")
shutil.rmtree('output_faces')