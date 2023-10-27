#include <opencv2/opencv.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/core.hpp>
#include <opencv2/imgproc.hpp>


# define M_PI           3.14159265358979323846  /* pi */

using namespace std;
using namespace cv;

// Функция Гаусса
double gauss(int x, int y, int a, int b, double sigma) {
    return (1 / (M_PI * 2 * sigma * sigma)) * exp(-((x - a) * (x - a) + (y - b) * (y - b)) / (2 * sigma * sigma));
}

// Mat — это основной класс данных для хранения изображений и других массивов в библиотеке OpenCV
// Нормализированная матрица Гаусса
Mat gaussian_matrix(int size, double sigma) {
    Mat matrix(size, size, CV_64F);
    double sum = 0;

    int half_size = size / 2;
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            matrix.at<double>(i, j) = gauss(i, j, half_size, half_size, sigma);
            sum += matrix.at<double>(i, j);
        }
    }
    matrix /= sum;
    return matrix;
}

// Свертка
Mat convolution(Mat img, Mat kernel) {
    Mat imgBlurred = img.clone();
    int ksize = kernel.rows;
    int x0 = ksize / 2;
    int y0 = ksize / 2;

    for (int i = x0; i < img.rows - x0; i++) {
        for (int j = y0; j < img.cols - y0; j++) {
            double val = 0;
            for (int m = -x0; m <= x0; m++) {
                for (int n = -y0; n <= y0; n++) {
                    // uchar часто используется для изображений в градациях серого
                    val += img.at<uchar>(i + m, j + n) * kernel.at<double>(m + x0, n + y0);
                }
            }
            imgBlurred.at<uchar>(i, j) = val;
        }
    }
    return imgBlurred;
}

// Реализация фильтра Гаусса
Mat my_gaussian_blur(Mat img, int size, double sigma) {
    int border = size / 2;
    Mat imgPadded;
    copyMakeBorder(img, imgPadded, border, border, border, border, BORDER_REFLECT);

    Mat kernel = gaussian_matrix(size, sigma);
    Mat imgBlurred = convolution(imgPadded, kernel);

    // ROI - обрезка изображения
    Rect regofinteres(border, border, img.cols, img.rows);
    return imgBlurred(regofinteres);
}

int main() {
    Mat img = imread("pic1.png", IMREAD_GRAYSCALE);
    if (img.empty()) {
        cout << "Ошибка при загрузке изображения!" << endl;
        return 1;
    }

    double sigma = 2.0;
    int ksize = 15;

    Mat Blur_img1 = my_gaussian_blur(img, 7, 7.0);
    imshow("Blur_img ksize = 7 sigma = 7", Blur_img1);


    Mat imgBlur_CV2;
    GaussianBlur(img, imgBlur_CV2, Size(ksize, ksize), sigma);

    imshow("Blur CV2", imgBlur_CV2);

    waitKey(0);
    return 0;
}
