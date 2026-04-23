import cv2
import mediapipe as mp

cv2.setUseOptimized(True)

mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)

cam = cv2.VideoCapture(0)

# Thresholds
eye_opening_threshold = 0.025
mouth_open_threshold = 0.03
squinting_threshold = 0.018

# Preload images (IMPORTANT for FPS)
cats = {
    "shock": cv2.imread("assets/cat-shock.jpeg"),
    "tongue": cv2.imread("assets/cat-tongue.jpeg"),
    "glare": cv2.imread("assets/cat-glare.jpeg"),
    "default": cv2.imread("assets/larry.jpeg")
}

# Metrics
def eye_metric(face):
    l_top = face.landmark[159]
    l_bot = face.landmark[145]
    r_top = face.landmark[386]
    r_bot = face.landmark[374]
    return (abs(l_top.y - l_bot.y) + abs(r_top.y - r_bot.y)) / 2.0


def mouth_metric(face):
    return abs(face.landmark[13].y - face.landmark[14].y)


def cat_shock(face):
    return eye_metric(face) > eye_opening_threshold


def cat_tongue(face):
    return mouth_metric(face) > mouth_open_threshold


def cat_glare(face):
    return eye_metric(face) < squinting_threshold


# Main Loop
def main():
    while True:
        ret, image = cam.read()
        if not ret:
            break

        image = cv2.flip(image, 1)

        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        result = face_mesh.process(rgb)

        # No face safety
        if not result.multi_face_landmarks:
            cv2.imshow("Face Camera", image)
            cv2.imshow("Cat Display", cats["default"])
            if cv2.waitKey(1) & 0xFF == 27:
                break
            continue

        face = result.multi_face_landmarks[0]

        # Draw landmarks (IMPORTANT for tracking clarity)
        h, w = image.shape[:2]
        for lm in face.landmark:
            x, y = int(lm.x * w), int(lm.y * h)
            cv2.circle(image, (x, y), 1, (0, 255, 0), -1)

        # Logic (priority system)
        if cat_tongue(face):
            cat_img = cats["tongue"]
        elif cat_shock(face):
            cat_img = cats["shock"]
        elif cat_glare(face):
            cat_img = cats["glare"]
        else:
            cat_img = cats["default"]

        # Show camera
        cv2.imshow("Face Camera", image)

        # Show cat window
        if cat_img is not None:
            cat_img = cv2.resize(cat_img, (640, 480))
            cv2.imshow("Cat Display", cat_img)
        else:
            blank = image * 0
            cv2.putText(blank, "Missing Image", (30, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 0, 255), 2)
            cv2.imshow("Cat Display", blank)

        # Exit on ESC
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()