import cv2
import os

def detect_face(file_name):
    img = cv2.imread(file_name)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    if len(faces) > 0:
        for i, (x, y, w, h) in enumerate(faces):
            wp = int(w/2)
            hp = int(h/2)
            cv2.rectangle(img, (x - wp, y - hp), (x + w + wp, y + h + hp), (255, 255, 255), 2)
            face = img[(y - hp):(y + h + hp),(x - wp):(x + w + wp)]
            cv2.imshow("Cropped Face", face)
            cv2.imwrite(f'output_images/{os.path.basename(file_name)} Face{i}.jpg', face)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    with os.scandir('./input_images') as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_file():
                try:
                    detect_face(f'input_images/{str(entry.name)}')
                except:
                    print(f'Unable to detect face in file [{str(entry.name)}].')

if __name__ == "__main__":
    main()
