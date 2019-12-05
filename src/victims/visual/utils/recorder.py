import cv2


class Camera:

    def __init__(self, n_camera):
        self.n_camera = n_camera

    @staticmethod
    def testCamera():
        out = []
        for i in range(0, 10):
            tcap = cv2.VideoCapture(i)
            test, _ = tcap.read()
            if test:
                out.append(i)
        return out

    def setCamera(self, n_camera):
        self.n_camera = n_camera

    def record(self, function, times):
        cap = cv2.VideoCapture(self.n_camera)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 300)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
        for i in range(times):
            ret, frame = cap.read()
            cv2.imshow('frame', frame)
            function(i, frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
