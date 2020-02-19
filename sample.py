#!/usr/bin/env python
# -*- coding: utf-8 -*-

import eel
import cv2 as cv
import base64

current_slide = 0


@eel.expose
def slide_change_event(val):
    global current_slide
    current_slide = val


def main():
    global current_slide

    cap = cv.VideoCapture(0)

    # EeLフォルダ設定、および起動 #########################################################
    eel.init('web')
    eel.start(
        'index.html',
        mode='chrome',
        cmdline_args=['--start-fullscreen'],
        block=False)

    while True:
        eel.sleep(0.01)

        # カメラキャプチャ ########################################################
        ret, frame = cap.read()
        if not ret:
            continue

        print(current_slide)

        # UI側へ転送 ##############################################################
        _, imencode_image = cv.imencode('.jpg', frame)
        base64_image = base64.b64encode(imencode_image)
        eel.set_base64image("data:image/jpg;base64," +
                            base64_image.decode("ascii"))

        key = cv.waitKey(1)
        if key == 27:  # ESC
            break


if __name__ == '__main__':
    main()
