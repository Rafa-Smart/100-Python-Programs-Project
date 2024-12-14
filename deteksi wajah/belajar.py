import cv2

camera = cv2.VideoCapture(0)
# camera.set(3, 460) # mengubah lebar camera, 3 = lebar
# camera.set(4, 480) # mengubah tinggi camera, 3 = tinggi

face_deteksi = cv2.CascadeClassifier("face_referensi.xml")
mata_deteksi = cv2.CascadeClassifier("mata_referensi.xml")

def close_window():
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        camera.release()
        cv2.destroyAllWindows()
        exit()
def main():
    while True:
        _,frame = camera.read()
        frame_abu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        wajah = face_deteksi.detectMultiScale(frame_abu, scaleFactor=1.1) # frame , scalefactor , minNeighbors

        # menggambar kotak
        for (x, y, w, h) in wajah:
            frame = cv2.rectangle(frame , (x,y) , (x + w,y + h) , (0,0,0), 3) 
            cv2.putText(frame, "hello sayang", (x + 80, y - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            mata_abu = frame_abu[y:y+h,x:x+w]
            mata_berwarna = frame[y:y+h,x:x+w]
            mata = mata_deteksi.detectMultiScale(mata_abu)
            for (x_mata,y_mata,w_mata,h_mata) in mata:
                cv2.rectangle(mata_berwarna, (x_mata,y_mata) , (x_mata + w_mata,y_mata + h_mata) , (255,0,0) , 2 )
                
            cv2.imshow("wajah mu sayang",frame)
            
            close_window()
if __name__ == "__main__":
    main()