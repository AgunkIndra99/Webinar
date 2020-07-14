import numpy as np
from numpy import array
from numpy import loadtxt
import math
import tflite_runtime.interpreter as tflite
import time


# pecah multivariate sequence menjadi sampel input dan target.
# Fungi diunduh ini dari https://machinelearningmastery.com/ karya Dr. Jason Brownlee
def split_sequences(sequences, n_steps_in, n_steps_out):
	X, y = list(), list()
	for i in range(len(sequences)):
		# find the end of this pattern
		end_ix = i + n_steps_in
		out_end_ix = end_ix + n_steps_out
		# check if we are beyond the dataset
		if out_end_ix > len(sequences):
			break
		# gather input and output parts of the pattern
		seq_x, seq_y = sequences[i:end_ix, :], sequences[end_ix:out_end_ix, :]
		X.append(seq_x)
		y.append(seq_y)
	return array(X), array(y)


filename_x = "data_x.csv"
filename_y = "data_y.csv"
dfx = loadtxt(filename_x, delimiter=',')
dfy = loadtxt(filename_y, delimiter=',')

scaled_test_x = dfx
scaled_test_y = dfy.reshape(-1,1)

# dummy untuk menyesuaikan dengan fungsi yang harus ada input minimal 2
dummy = np.concatenate((scaled_test_y,scaled_test_y),axis=1) 
dataset_test = np.concatenate((scaled_test_x,dummy),axis=1)

# choose a number of time steps
n_steps_in = 4  # Berapa jam yang sudah berlalu yang dipakai untuk mempredisi kedepan?
n_steps_out = 1 # 1 = predict 1 jam, 3 = predict 1-3 jam, dsb
n_output = 1    # berapa fitur yg akan ditargetkan
h_predict = 0   # maksimal 23

m_data_test_x, m_data_test_y = split_sequences(dataset_test, n_steps_in, n_steps_out)
# Cari Inputnya saja
data_test_x = m_data_test_x[:,:,:-2]
# Cari Targetnya saja
data_test_y = m_data_test_y[:,:,23]


energy_model = tflite.Interpreter(model_path='modelEnergyPrediction.tflite')
energy_model.allocate_tensors()

# Dapatkan input dan output tensors.
input_details = energy_model.get_input_details()
output_details = energy_model.get_output_details()

i = 0
try:
    while True:
        input_data = np.array(data_test_x[i], dtype=np.float32)
        input_data = np.expand_dims(input_data, axis=0)
        energy_model.set_tensor(input_details[0]['index'], input_data)
        energy_model.invoke()
        output_data = energy_model.get_tensor(output_details[0]['index'])
        printDataPred = np.squeeze(output_data.round(2))
        printDataAktual = np.squeeze(data_test_y[i])
        print(f'Aktual: {printDataAktual} --- Prediksi: {printDataPred}')
        time.sleep(1.0)
        i = i + 1
        
        # Ulangi jika data uji lebih dari 3500
        if i > 3500:
            i = 0

except KeyboardInterrupt:

    pass

