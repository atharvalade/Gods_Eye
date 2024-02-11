**God's Eye - Intelligent Surveillance System**

**Overview**

Welcome to God's Eye, a cutting-edge solution for intelligent surveillance. This project aims to provide a sophisticated software tool for legal authorities, including police, city councils, and legal entities, to efficiently analyze CCTV footage and identify perpetrators, victims, witnesses, or any specific individuals of interest. God's Eye employs advanced facial recognition technology to condense lengthy hours of surveillance footage into concise, relevant clips, saving time and effort for law enforcement professionals.

**Features**

Facial Recognition: Utilizes a complex algorithm to recognize faces within CCTV footage.
Timestamp Analysis: Provides specific timestamps with identified faces for easy reference.
Output Video Creation: Generates a compiled video containing identified individuals based on timestamps.
User-Friendly: Simplifies the process of sifting through surveillance footage to locate critical moments.
Getting Started

**To use God's Eye, follow these steps:**

Clone the Repository:
bash
Copy code
git clone https://github.com/your-username/gods-eye.git
cd gods-eye
Install Dependencies:
bash
Copy code
pip install -r requirements.txt
Run the Code:
bash
Copy code
python gods_eye.py
Provide Input:
Replace perp1.jpg with the reference image of the person of interest.
Specify the path to the CCTV video in video_path variable.
Review Output:
Check the console for match results.
Find the sorted timestamps in the console output.
Locate the compiled output video at the specified path.

**Code Explanation**

The Python script gods_eye.py performs the following tasks:
Captures frames from the provided CCTV video.
Utilizes facial recognition to identify faces in specific frames.
Creates individual face images and timestamps for matching faces.
Compiles a sorted list of timestamps with matching faces.
Generates an output video containing identified individuals.

**Note**

Ensure the availability of a facial reference image (perp1.jpg) and a valid CCTV video file (video_path) for accurate results.
Adjust the skip_factor variable to control the frequency of frame analysis for efficiency.

**Output**

The output video will be saved as output_video.mp4.
Temporary face images are stored in the output_faces directory during the process and cleaned up afterward.

**Disclaimer**

This project is intended for legal and ethical use only. It is crucial to comply with privacy laws and regulations when deploying surveillance technologies.

Feel free to contribute, report issues, or suggest improvements. Happy surveilling!
