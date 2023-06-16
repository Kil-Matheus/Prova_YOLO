import cv2
from ultralytics import YOLO

input_video = cv2.VideoCapture('p2-pratica-main/assets/arsene.mp4')
model = YOLO("yolov8n.pt")

width  = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret, frame= input_video.read()
    result = model.predict(frame, conf = 0.5)
    output_video = cv2.VideoWriter( './p2-pratica-main/exemplos/saida/out.avi',cv2.VideoWriter_fourcc(*'DIVX'), 24, (width, height))
    output_video.write(frame)
    
    if not ret:
        break
    
    cv2.imshow('Video Playback', result[0].plot())
    
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
    
output_video.release()
input_video.release()
cv2.destroyAllWindows()