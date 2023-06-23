import face_alignment
import cv2
from argparse import ArgumentParser

CIRCLE_SIZE = 4

def get_image_alignment(image_path):
    fa = face_alignment.FaceAlignment(face_alignment.LandmarksType.TWO_D, flip_input=False)
    image = cv2.imread(image_path)
    preds = fa.get_landmarks(image)
    return image, preds


def visualize_plots(image, preds_alignment, output_path):
    for point in preds_alignment[0]:
        cv2.circle(image, (int(point[0]), int(point[1])), CIRCLE_SIZE, (0, 255, 255),thickness=-1, lineType=cv2.FILLED)

    cv2.imwrite(output_path, image)


def main():
    parser = ArgumentParser()
    parser.add_argument('--input', default=None, type=str, help='input image path')
    parser.add_argument('--output', default=None, type=str, help='output image path')
    args = parser.parse_args()
    image, preds = get_image_alignment(args.input)
    visualize_plots(image, preds, args.output)

if __name__=='__main__':
    main()
