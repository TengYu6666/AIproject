#include <opencv2/opencv.hpp>
#include <opencv2/dnn.hpp>
#include <iostream>
#include <string>

using namespace cv;
using namespace cv::dnn;
using namespace std;

int main() {
    // 模型和图片路径
    string model_path = "E:\\opencv推理\\tuilimoxing\\resnet18_imagenet.onnx";
    string image_path = "E:\\opencv推理\\tuilimoxing\\putao.jpg";

    // 加载ONNX模型
    cout << "Loading model: " << model_path << endl;
    Net net = readNetFromONNX(model_path);
    if (net.empty()) {
        cerr << "Error: Failed to load model!" << endl;
        return -1;
    }
    cout << "Model loaded successfully." << endl;

    // 设置计算后端和目标设备
    net.setPreferableBackend(DNN_BACKEND_OPENCV);
    net.setPreferableTarget(DNN_TARGET_CPU);

    // 读取图片
    cout << "Loading image: " << image_path << endl;
    Mat image = imread(image_path);
    if (image.empty()) {
        cerr << "Error: Failed to load image!" << endl;
        return -1;
    }
    cout << "Image loaded successfully. Size: " << image.size() << endl;

    // 图片预处理 - ResNet18标准预处理
    Mat blob;
    Size input_size(224, 224);

    // 1. Resize到256x256
    Mat resized_img;
    resize(image, resized_img, Size(256, 256));

    // 2. CenterCrop到224x224
    Rect crop_region((resized_img.cols - 224) / 2, (resized_img.rows - 224) / 2, 224, 224);
    Mat cropped_img = resized_img(crop_region);

    // 3. 归一化 - 使用PyTorch预训练模型的参数
    Scalar mean(0.485 * 255, 0.456 * 255, 0.406 * 255); // BGR顺序
    Scalar std(0.229 * 255, 0.224 * 255, 0.225 * 255);   // BGR顺序

    blobFromImage(cropped_img, blob, 1.0 / 255.0, input_size, mean, true, false, CV_32F);
    blob /= Scalar(std[0] / 255.0, std[1] / 255.0, std[2] / 255.0);

    // 设置模型输入
    net.setInput(blob);

    // 执行推理
    cout << "Running inference..." << endl;
    Mat output;
    net.forward(output);

    // 处理输出结果
    Point class_id;
    double confidence;
    minMaxLoc(output.reshape(1, 1), nullptr, &confidence, nullptr, &class_id);

    // 输出结果
    cout << "\n=== Inference Result ===" << endl;
    cout << "Predicted class ID: " << class_id.x << endl;
    cout << "Confidence: " << confidence << endl;
    cout << "========================" << endl;

    return 0;
}