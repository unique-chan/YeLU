import tensorflow as tf
from tensorflow.keras import layers

from loader import train_test, train_valid_test
from parser import parse_args
from network import network


# Parser
args = parse_args()

# Loader
train_ds, valid_ds, test_ds = None, None, None

if args.cv_mode == 'train-test':
    train_ds, test_ds = train_test(args)
else:
    train_ds, valid_ds, test_ds = train_valid_test(args)

# Number of Classes
args.num_classes = len(train_ds.class_names)
print(args)

# Network
model = network(args)
print(model)

# Train / Eval
# trainer = Trainer(...)
# train_eval(trainer, args)
