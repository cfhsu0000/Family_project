import cv2

url = 'https://cctvatis4.ntpc.gov.tw/C000267'
# low resolution Family
# https://cctvtraffic.tycg.gov.tw/camera155/
cap = cv2.VideoCapture(url)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('morning_1230.mp4', fourcc, 20.0, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break



cap.release()
out.release()
cv2.destroyAllWindows()
