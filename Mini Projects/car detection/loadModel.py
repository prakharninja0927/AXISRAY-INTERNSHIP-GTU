import cv2 as cv

class CarDetector:

    def __init__(self):
        # Load algo
        algo = cv.dnn.readNet("dnn_model/yolov4.cfg", "dnn_model/yolov4.weights")
        self.model = cv.dnn_DetectionModel(algo)
        self.model.setInputParams(size=(832, 832), scale=2.4 / 255)
        ''' size	New input size.
            scale	Multiplier for frame values.
        '''
        # Allow classes containing car only
        self.classes_allowed = [2] # here id for car class is 2 hence we only need to detect car hence it is written 2.

    def detect_cars(self, img):
        # Detect Objects
        cars_boxes = []
        class_ids, confidence, boxes = self.model.detect(img, nmsThreshold=0.4)
        zipVar = zip(class_ids, confidence, boxes)
        for class_id, confidence, box in zipVar:
            if confidence < 0.5:
                # Skip detection with low confidence
                continue

            if class_id in self.classes_allowed:
                cars_boxes.append(box)

        return cars_boxes
