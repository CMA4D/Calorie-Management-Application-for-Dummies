# Calorie-Management-Application-for-Dummies
It's literally in the name!
##树莓派脚本
功能基本完成，功能简介：
http协议小服务器 地址http://<主机ip>:8080 (注树莓派固定ip地址为10.29.113.246，即访问设备端地址为http://10.29.113.246:8080)
 get 请求/capture捕获并发送图片，请求/measure测量质量并以报文形式发回，请求/download下载上次所拍照片，请求/upload上传图片给服务器
服务器根页面提供上传图片，下载图片，拍摄图片请求按钮，请求功能如上；显示当前测量的质量，提供刷新按钮以重新测量并显示；提供输入框和提交按钮以校准hx711的参数并重新初始化。
