import neural_network
import functions
import numpy as np


def training():
    _train_data, _train_labels, _test_data, _test_labels = functions.load_trainig_data()
    print("Training entries: {}, labels: {}".format(len(_train_data), len(_train_labels)))
    _word_index = functions.get_word_settings()
    _train_data = functions.format_sequence_elements(_train_data, _word_index)
    _test_data = functions.format_sequence_elements(_test_data, _word_index)
    print(len(_train_data[0]), len(_train_data[1]))

    _train_x, _train_y, _test_x, _test_y = functions.splitting(_train_data, _train_labels)

    _model = neural_network.build(functions.get_num_values())
    _model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    _model.fit(_train_x, _train_y, epochs=40, batch_size=512, validation_data=(_test_x, _test_y), verbose=1)
    _model.evaluate(_test_data, _test_labels)
    _model.save(f'models/model')

def prodution():
    _model = neural_network.load()
    print(_model.predict(np.array(['Brasil', 'Dinheiro'])))

if __name__ == "__main__":
    # training()
    prodution()