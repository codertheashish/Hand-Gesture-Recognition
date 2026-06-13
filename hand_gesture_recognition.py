import cv2
import mediapipe as mp
import math

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

def fingers_up(landmarks):
    fingers = []

    # Thumb - distance based check
    thumb_tip = landmarks[4]
    wrist = landmarks[0]
    mcp = landmarks[2]
    
    dist_tip = math.hypot(thumb_tip.x - wrist.x, thumb_tip.y - wrist.y)
    dist_mcp = math.hypot(mcp.x - wrist.x, mcp.y - wrist.y)
    
    if dist_tip > dist_mcp * 1.3:
        fingers.append(1)
    else:
        fingers.append(0)

    tips = [8, 12, 16, 20]
    pips = [6, 10, 14, 18]
    for tip, pip in zip(tips, pips):
        if landmarks[tip].y < landmarks[pip].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers

def classify_gesture(fingers, landmarks):
    thumb, index, middle, ring, pinky = fingers
    if thumb == 1 and sum(fingers[1:]) == 0:
        if landmarks[4].y < landmarks[0].y:
            return "Thumbs Up"
        else:
            return "Thumbs Down"
    if index == 1 and middle == 0 and ring == 0 and pinky == 1 and thumb == 0:
        return "Swag"
    if sum(fingers) == 0:
        return "Fist"
    if index == 1 and middle == 1 and ring == 0 and pinky == 0 and thumb == 0:
        return "Peace Sign"
    if index == 1 and middle == 0 and ring == 0 and pinky == 0:
        return "Pointing Finger"
    if sum(fingers) == 5:
        return "Open Hand"
    dist = math.hypot(landmarks[4].x - landmarks[8].x, landmarks[4].y - landmarks[8].y)
    if dist < 0.05 and middle == 1 and ring == 1 and pinky == 1:
        return "OK"
    return "Unknown"

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        break
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    gesture = "No Hand"
    total_fingers = 0

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            landmarks = hand_landmarks.landmark
            fingers = fingers_up(landmarks)
            total_fingers += sum(fingers)

        if len(result.multi_hand_landmarks) == 1:
            landmarks = result.multi_hand_landmarks[0].landmark
            fingers = fingers_up(landmarks)
            gesture = classify_gesture(fingers, landmarks)
        else:
            gesture = "Two Hands"

    # Both hands open (10 fingers) -> exit
    if len(result.multi_hand_landmarks or []) == 2 and total_fingers == 10:
        cv2.putText(img, "10 Fingers - Exiting", (30, 60), cv2.FONT_HERSHEY_SIMPLEX,
                    1.3, (0, 0, 255), 3)
        cv2.imshow("Hand Gesture Recognition", img)
        cv2.waitKey(1500)
        break

    cv2.putText(img, gesture, (30, 60), cv2.FONT_HERSHEY_SIMPLEX,
                1.5, (0, 255, 0), 3)
    cv2.imshow("Hand Gesture Recognition", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()