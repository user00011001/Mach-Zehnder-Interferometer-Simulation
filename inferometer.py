import strawberryfields as sf
from strawberryfields import ops
from math import pi

# Common phase settings and state preparations
common_phases = [0, pi/2, pi, 3*pi/2, 2*pi]
state_preparations = ['Single Photon State', 'Coherent State']


def get_input():
    print("Choose from the following common phase settings:")
    for i, phase in enumerate(common_phases):
        print(f"{i}: Phase = {phase}")
    choice = int(
        input("Enter the number of your choice for the phase in the first mode: "))
    phase1 = common_phases[choice]
    choice = int(
        input("Enter the number of your choice for the phase in the second mode: "))
    phase2 = common_phases[choice]

    print("Choose from the following state preparations:")
    for i, state in enumerate(state_preparations):
        print(f"{i}: {state}")
    choice = int(
        input("Enter the number of your choice for state preparation: "))
    state_preparation = state_preparations[choice]

    return phase1, phase2, state_preparation


def main():
    phase1, phase2, state_preparation = get_input()

    # initialize a 2-mode quantum program
    prog = sf.Program(2)

    with prog.context as q:
        # Prepare the chosen state in the first mode
        if state_preparation == 'Single Photon State':
            ops.Fock(1) | q[0]
        elif state_preparation == 'Coherent State':
            ops.Coherent(1) | q[0]

        # First beam splitter
        ops.BSgate(pi/4, 0) | (q[0], q[1])

        # Phase shifters
        ops.Rgate(phase1) | q[0]
        ops.Rgate(phase2) | q[1]

        # Second beam splitter
        ops.BSgate(pi/4, 0) | (q[0], q[1])

    # initialize a quantum simulator
    eng = sf.Engine('fock', backend_options={"cutoff_dim": 5})

    result = eng.run(prog)

    # get the state of the quantum register
    state = result.state

    # print the most probable photon number for each mode
    print("Most probable photon number for Mode 0:")
    probs = [state.fock_prob([n, 0]) for n in range(5)]
    print(f"{probs.index(max(probs))} photons")

    print("Most probable photon number for Mode 1:")
    probs = [state.fock_prob([0, n]) for n in range(5)]
    print(f"{probs.index(max(probs))} photons")


if __name__ == "__main__":
    main()
