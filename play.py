import cv2

def play(video):

    #フレーム数，フレームレートを取得
    frame_count = int(video.get(7))
    frame_rate = int(video.get(5))

    cv2.namedWindow('player', cv2.WINDOW_AUTOSIZE)#ウィンドウの設定

    for i in range(frame_count):
        is_read, frame = video.read()#1フレーム取得

        k=cv2.waitKey(frame_rate)
        if k == 27 or not is_read:
            break
        cv2.imshow("player", frame)
