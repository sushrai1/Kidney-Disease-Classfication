import os
import tensorflow as tf
from cnnClassifier.entity.config_entity import TrainingConfig
from pathlib import Path

class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config
        self.model = None
        self.train_generator = None
        self.valid_generator = None
        self.steps_per_epoch = None
        self.validation_steps = None

    def get_base_model(self):
        try:
            print(f"Loading base model from: {self.config.updated_base_model_path}")
            self.model = tf.keras.models.load_model(self.config.updated_base_model_path)
            print("Base model loaded successfully.")
        except Exception as e:
            print(f"Error loading base model: {e}")
            raise

    def train_valid_generator(self):
        datagenerator_kwargs = dict(
            rescale=1. / 255,
            validation_split=0.2
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation='bilinear'
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset='validation',
            shuffle=False,
            **dataflow_kwargs
        )

        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs
            )
            print("Using data augmentation for training data.")
        else:
            train_datagenerator = valid_datagenerator
            print("No data augmentation applied.")

        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset='training',
            shuffle=True,
            **dataflow_kwargs
        )

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        os.makedirs(path.parent, exist_ok=True)
        model.save(path)
        print(f"Model saved at: {path}")

    def train(self):
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        print(f"Training for {self.config.params_epochs} epochs...")
        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.valid_generator
        )

        self.save_model(path=self.config.trained_model_path, model=self.model)