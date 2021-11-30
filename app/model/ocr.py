import cv2 
import pytesseract
import numpy as np
from scipy.ndimage import interpolation as inter


class OCR:
    @staticmethod
    def read_image(path):
        return cv2.imread(path)

    @staticmethod
    def correct_skew(image, delta=1, limit=5):
        def determine_score(arr, angle):
            data = inter.rotate(arr, angle, reshape=False, order=0)
            histogram = np.sum(data, axis=1)
            score = np.sum((histogram[1:] - histogram[:-1]) ** 2)
            return histogram, score

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1] 

        scores = []

        angles = np.arange(-limit, limit + delta, delta)
        for angle in angles:
            histogram, score = determine_score(thresh, angle)
            scores.append(score)

        best_angle = angles[scores.index(max(scores))]

        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, best_angle, 1.0)
        rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

        return best_angle, rotated

    @staticmethod
    def get_grayscale(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    @staticmethod
    def get_rgb(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    @staticmethod
    def equalize_hist(image):
        return cv2.equalizeHist(image)

    @staticmethod
    def otsu_threshold(image):
        return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    @staticmethod
    def adaptive_threshold(image):
        return cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

    @staticmethod
    def image_to_string(path):
        image = OCR.read_image(path)
        angle,image = OCR.correct_skew(image)
        image = OCR.get_grayscale(image)
        image = OCR.otsu_threshold(image)

        custom_config =  r'-l ind --psm 6'
        filtered = []
        try:
            d = pytesseract.image_to_string(image, config=custom_config, timeout=5)
            clear_data = d.split('\n')
            
            for item in clear_data:
                if item.isspace() or len(item) <= 2:
                    continue
                else:
                    filtered.append(item)
        except RuntimeError as timeout_error:
            return None

        return filtered
        