### TensorFlow in Practice勘误

对编程作业中错误之处的记录:
- Exercises (2020.04.20)
   - Exercise 6 - Answer中，`shuffled_set[:testing_length]`应改为`shuffled_set[-testing_length:]`；验证集图片不应该被增强，`validation_datagen = ImageDataGenerator(rescale=1./255)`即可
   - Exercise 7 - Answer中，在声明train_dir之前，对其进行了调用