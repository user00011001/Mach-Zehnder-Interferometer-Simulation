import strawberryfields as sf
from strawberryfields.ops import Dgate, BSgate, Rgate, MeasureFock

def run_quantum_interference(phi_0, phi_1, alpha_0, alpha_1, shots=1):

    prog = sf.Program(2)

    with prog.context as q:
        Dgate(alpha_0) | q[0]
        Dgate(alpha_1) | q[1]

        BSgate(0.5, 0) | (q[0], q[1])


        Rgate(phi_0) | q[0]
        Rgate(phi_1) | q[1]

        BSgate(0.5, 0) | (q[0], q[1])

        MeasureFock() | q[0]
        MeasureFock() | q[1]

    eng = sf.Engine(backend="gaussian")
    result = eng.run(prog, shots=shots)

    return result

def get_user_input(prompt, options):
    while True:
        print(prompt)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        choice = input("Enter your choice (1-{}): ".format(len(options)))
        try:
            index = int(choice) - 1
            if 0 <= index < len(options):
                return options[index]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

phase_options = [0, 0.5, 1, 1.5, 2]
alpha_options = [0, 0.5, 1, 1.5, 2]

phi_0 = get_user_input("Select the phase setting for mode 0 (in radians):", phase_options)
phi_1 = get_user_input("Select the phase setting for mode 1 (in radians):", phase_options)
alpha_0 = get_user_input("Select the displacement amplitude for mode 0:", alpha_options)
alpha_1 = get_user_input("Select the displacement amplitude for mode 1:", alpha_options)

num_shots = 1000
results = run_quantum_interference(phi_0, phi_1, alpha_0, alpha_1, shots=num_shots)

mode_0_counts = {}
mode_1_counts = {}

for i in range(num_shots):
    mode_0_photon = results.samples[i][0]
    mode_1_photon = results.samples[i][1]

    mode_0_counts[mode_0_photon] = mode_0_counts.get(mode_0_photon, 0) + 1
    mode_1_counts[mode_1_photon] = mode_1_counts.get(mode_1_photon, 0) + 1

print("Measurement results:")
print("Mode 0 photon number distribution:", mode_0_counts)
print("Mode 1 photon number distribution:", mode_1_counts)
