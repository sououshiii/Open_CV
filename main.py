import cv2

frame_width = 640
frame_height = 480
min_area = 150

plate_number = cv2.CascadeClassifier("/Users/mac/PycharmProjects/OpenCv_Project/Project_2/haar_cascade_ru.xml")
video = cv2.VideoCapture("/Users/mac/PycharmProjects/OpenCv_Project/Project_2/Movie.mp4")
video.set(3, frame_width)
video.set(4, frame_height)
counter = 1


while True:
    success, img = video.read()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plates = plate_number.detectMultiScale(img_gray, 1.1, 10)
    for (x, y, width, height) in plates:
        area = width*height
        if area > min_area:
            cv2.rectangle(img, (x, y), (x+width, y+height), (0, 0, 255), 5)
            plate_detected = img[y:y+height, x:x+width]

    cv2.imshow("Detection", img)
    if cv2.waitKey(1) & 0XFF == ord('s'):
        cv2.imwrite("/Users/mac/PycharmProjects/OpenCv_Project/Project_2/image{}.jpg".format(counter), plate_detected)
        counter += 1
